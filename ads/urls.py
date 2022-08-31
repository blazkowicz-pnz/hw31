from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from ads.views.ads import AdListView, AdDetailView
from ads.views.category import CategoriesViewSet
from ads.views.location import LocationsViewSet
from ads.views.service import root
from ads.views.ads import  AdCreateView, AdUpdateView, AdDeleteView, AdUploadImage
from ads.views.users import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView
from home_w27 import settings

router = routers.SimpleRouter()
router.register("location", LocationsViewSet)
router.register("category", CategoriesViewSet)

urlpatterns = [
    path('', root),
    path("", include(router.urls)),
    path('ad/', AdListView.as_view()),
    path("ad/<int:pk>/", AdDetailView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdUploadImage.as_view()),
    path("user/", UserListView.as_view()),
    path("user/<int:pk>/", UserDetailView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', UserDeleteView.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)