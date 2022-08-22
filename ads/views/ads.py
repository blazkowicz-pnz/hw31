import json

from django.core.paginator import Paginator
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from ads.models import Category, Ad, User
from home_w27 import settings


class AdListView(ListView):
    model = Ad
    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related("author").order_by("price")
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 0)
        page_obj = paginator.get_page(page_number)

        ads = []

        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "image": ad.image.url if ad.image else None
            })

        response = {
            "items": ads,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }
        return JsonResponse(response, safe=False)



class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "image": ad.image.url if ad.image else None
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class AdCreateView(CreateView):
    model = Ad
    fields = ("name", "author", "price", "description", "is_published", "category")

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

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


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateView):
    model = Ad
    fields = fields = ("name", "author", "price", "description", "is_published", "category")

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.name = ad_data["name"],
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        self.object.author = get_object_or_404(User, pk=ad_data["author_id"])
        self.object.category = get_object_or_404(Category, pk=ad_data["category_id"])
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        })



# @method_decorator(csrf_exempt, name="dispatch")
# class AdsView(View):
#     def get(self, request):
#         all_ads = Ad.objects.all()
#
#         res = []
#         for ad in all_ads:
#             res.append({
#                 "id": ad.id,
#                 "name": ad.name,
#                 "author": ad.author,
#                 "price": ad.price,
#                 "description": ad.description,
#                 "address": ad.address,
#                 "is_published": ad.is_published
#             })
#         return JsonResponse(res, safe=False, json_dumps_params={"ensure_ascii": False})
#
#     def post(self, request):
#         data = json.loads(request.body)
#         new_ad = Ad.objects.create(name=data["name"],
#                                     author=data["author"],
#                                     price=data["price"],
#                                     description=data["description"],
#                                     address=data["address"],
#                                     is_published=data["is_published"]
#                                     )
#         return JsonResponse({
#                 "id": new_ad.id,
#                 "name": new_ad.name,
#                 "author": new_ad.author,
#                 "price": new_ad.price,
#                 "description": new_ad.description,
#                 "address": new_ad.address,
#                 "is_published": new_ad.is_published},
#             safe=False,
#             json_dumps_params={"ensure_ascii": False})
#
#
# class AdDetailView(DetailView):
#     model = Ad
#
#     def get(self, request, *args, **kwargs):
#         try:
#             ad = self.get_object()
#         except Exception:
#             return JsonResponse({"error": "item not found"}, status=404)
#
#         return JsonResponse({
#                    "id": ad.id,
#                    "name": ad.name,
#                    "author": ad.author,
#                    "price": ad.price,
#                    "description": ad.description,
#                    "address": ad.address,
#                    "is_published": ad.is_published},
#             safe=False,
#             json_dumps_params={"ensure_ascii": False}
#         )
#
#
# class CategoryDetailView(DetailView):
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         try:
#             cat = self.get_object()
#         except Exception:
#             return JsonResponse({"error": "item not found"}, status=404)
#
#         return JsonResponse({
#                     "id": cat.id,
#                     "name": cat.name},
#                 safe=False,
#                 json_dumps_params={"ensure_ascii": False})
#
#
