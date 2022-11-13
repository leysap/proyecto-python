from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ver-libros/', views.ver_libros, name='ver_libros'),
    path('nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
    path('cargar-libro/', views.CargarLibro.as_view(), name='cargar_libro'),
    path('editar/<int:pk>', views.EditarLibro.as_view(), name='editar_libro'),
    path('eliminar/<int:pk>', views.EliminarLibro.as_view(), name='eliminar_libro'),
    path('ver_libro/<int:pk>', views.VerLibro.as_view(), name='ver_libro'),

]