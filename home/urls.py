from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    path('ver-personas/', views.ver_personas),
]