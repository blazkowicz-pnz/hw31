import json
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ads.models import User, Location
# from ads.serializers import UserListSerializer
from ads.serializers import UserCreateSerializer
from home_w27 import settings
from rest_framework.generics import CreateAPIView



class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         self.object_list = self.object_list.prefetch_related("location")\
#             .annotate(total_ads=Count("ad__is_published"
#             , filter=Q(ad__is_published=True))).order_by("username")
#
#         paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
#         page_number = request.GET.get("page", 0)
#         page_obj = paginator.get_page(page_number)
#
#         users = []
#
#         for user in page_obj:
#             users.append({
#                 "id": user.id,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "role": user.role,
#                 "age": user.age,
#                 "locations": list(map(str, user.location.all())),
#                 "total_ads": user.total_ads,
#
#             })
#
#         response = {
#             "items": users,
#             "num_pages": page_obj.paginator.num_pages,
#             "total": page_obj.paginator.count,
#         }
#         return JsonResponse(response, safe=False)
#
#
# class UserDetailView(DetailView):
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         user = self.get_object()
#
#         return JsonResponse({
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "role": user.role,
#             "age": user.age,
#             "locations": list(map(str, user.location.all()))
#
#         })
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class UserCreateView(CreateView):
#     model = User
#     fields = ("username", "password", "first_name", "last_name", "role", "age", "locations")
#
#     def post(self, request, *args, **kwargs):
#         user_data = json.loads(request.body)
#
#         new_user = User.objects.create(
#             username=user_data["username"],
#             password=user_data["password"],
#             first_name=user_data["first_name"],
#             last_name=user_data["last_name"],
#             role=user_data["role"],
#             age=user_data["age"],
#
#         )
#
#         for location in user_data["locations"]:
#             loc_obj, created = Location.objects.get_or_create(
#                 name=location,
#             )
#             new_user.location.add(loc_obj)
#         new_user.save()
#
#         return JsonResponse({
#             "id": new_user.id,
#             "username": new_user.username,
#             "first_name": new_user.first_name,
#             "last_name": new_user.last_name,
#             "role": new_user.role,
#             "age": new_user.age,
#             "locations": list(map(str, new_user.location.all()))
#
#         })
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ("username", "password", "first_name", "last_name", "age", "location")
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#
#         user_data = json.loads(request.body)
#         self.object.location.set([])
#         self.object.username = user_data["username"]
#         self.object.password = user_data["password"]
#         self.object.first_name = user_data["first_name"]
#         self.object.last_name = user_data["last_name"]
#         self.object.age = user_data["age"]
#
#         if user_data["locations"]:
#             for location in user_data["locations"]:
#                 loc_obj, created = Location.objects.get_or_create(
#                     name=location,
#
#                 )
#                 self.object.location.add(loc_obj)
#         self.object.save()
#
#         return JsonResponse({
#             "id": self.object.id,
#             "username": self.object.username,
#             "first_name": self.object.first_name,
#             "last_name": self.object.last_name,
#             "age": self.object.age,
#             "locations": list(map(str, self.object.location.all()))
#         })
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class UserDeleteView(DeleteView):
#     model = User
#     success_url = "/"
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({
#             "status": "ok"
#         }, status=204)