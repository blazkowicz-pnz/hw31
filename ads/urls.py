from django.urls import path
from django.conf.urls.static import static

from ads.views import CategoryView, root, AdsView, CategoryDetailView, AdDetailView
from home_w27 import settings

urlpatterns = [
    path('', root),
    path('cat/', CategoryView.as_view()),
    path('ad/', AdsView.as_view()),
    path('cat/<int:pk>', CategoryDetailView.as_view()),
    path('ad/<int:pk>', AdDetailView.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)