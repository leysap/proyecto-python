from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cargar-libro/', views.cargar_libro, name='cargar_libro'),
    path('ver-libros/', views.ver_libros, name='ver_libros'),
    path('about/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
]