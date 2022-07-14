from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.photography, name="photography"),
    path('portfolio', views.home, name="portfolio"),
	path('portfolio/projects/', views.projects, name="projects"),
	path('portfolio/project/<slug:slug>/', views.project, name="project"),
    path('gallery', views.gallery, name="gallery"),
    path('photo/<str:pk>/', views.viewPhoto, name="photo"),
    path('privacy_policy', views.PrivacyPolicy, name="privacy_policy")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)