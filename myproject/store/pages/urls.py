from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('phone',views.phone),
    path('computer',views.computer),
    path('tablet',views.tablet),
    path('accesory',views.accesory),
    path('index', views.index),
    path('contact',views.contact),
    path('about', views.about),

]