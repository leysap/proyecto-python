from django.urls import path
from home import views

urlpatterns = [
    #VERSION VISTAS
    path('', views.index, name="index"),
    # path('cargar-libro/', views.cargar_libro, name='cargar_libro'),
    path('ver-libros/', views.ver_libros, name='ver_libros'),
    # path('editar/<int:id>', views.editar_libro, name='editar_libro'),
    # path('eliminar/<int:id>', views.eliminar_libro, name='eliminar_libro'),
    path('nosotros/', views.acerca_de_nosotros, name='acerca_de_nosotros'),
       
    #VERSION CLASES BASADAS EN VISTAS   
    # path('ver-libros/', views.ListaLibros.as_view(), name='ver_libros'),
    path('cargar-libro/', views.CargarLibro.as_view(), name='cargar_libro'),
    path('editar/<int:pk>', views.EditarLibro.as_view(), name='editar_libro'),
    path('eliminar/<int:pk>', views.EliminarLibro.as_view(), name='eliminar_libro'),
    path('ver_libro/<int:pk>', views.VerLibro.as_view(), name='ver_libro'),

]