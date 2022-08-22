from django.urls import path
from django.conf.urls.static import static
from ads.views.service import root
from ads import views
from ads.views.category import CategoryListView, CategoryDeleteView, CategoryCreateView, CategoryUpdateView, CategoryDetailView
from home_w27 import settings

urlpatterns = [
    path('', root),
    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
    # path('ad/', AdsView.as_view()),
    #
    # path('ad/<int:pk>', AdDetailView.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)