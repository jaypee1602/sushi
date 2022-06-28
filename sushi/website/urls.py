from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('menu', views.menu, name="menu"),
    path('contact', views.contact, name="contact"),
    path('delivery', views.delivery, name="delivery"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
