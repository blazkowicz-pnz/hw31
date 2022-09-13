import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView
from ads.models import Category, Ad, User
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from ads.permissions import AdUpdateDeletePermission
from ads.serializers.ad import AdSerializer, AdDetailSerializer
from rest_framework.permissions import IsAuthenticated


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


    def get(self, request, *args, **kwargs):
        categories = request.GET.getlist("cat", [])
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        text = request.GET.get("name")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get("locations")
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)
        price_from = request.GET.get("price_from")
        price_to = request.GET.get("price_to")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=int(price_from))
        if price_to:
            self.queryset = self.queryset.filter(price__lte=int(price_to))
        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ad
    fields = ("name", "author", "price", "description", "is_published", "category")

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        if ad_data["is_published"] is True:
            return JsonResponse({"error": "bad status"},status=400)

        new_ad = Ad.objects.create(
            name=ad_data["name"],
            author=get_object_or_404(User, pk=ad_data["author_id"]),
            price=ad_data["price"],
            description=ad_data["description"],
            is_published=ad_data["is_published"],
            category=get_object_or_404(Category, pk=ad_data["category_id"]),
        )

        return JsonResponse({
            "id": new_ad.id,
            "name": new_ad.name,
            "author": new_ad.author_id,
            "price": new_ad.price,
            "description": new_ad.description,
            "is_published": new_ad.is_published,
            "category": new_ad.category_id,
            "image": new_ad.image.url if new_ad.image else None
        })


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, AdUpdateDeletePermission]
    serializer_class = AdSerializer


@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({}, status=204)


@method_decorator(csrf_exempt, name="dispatch")
class AdUploadImage(UpdateView):
    model = Ad
    fields = ("image",)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get("image", None)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        })


