

from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projectPage, name='projects'),
    path('constructionPics/', views.constructionPics, name='constructionPics'),
    path('elevationPics/', views.elevationPics, name='elevationPics'),
    path('interiorPics/', views.interiorPics, name='interiorPics'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contactUs/', views.contactUs, name='contactUs'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

