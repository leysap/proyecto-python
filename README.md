<!-- PARA IR COMPLETANDO -->
# BLOG DE LIBROS

Proyecto realizado con Python usando Django en el curso de Coderhouse.
Se trata de un blog para poder cargar libros, guardarlos en una base de datos y poder visualizarlos.

## ¿Como se levanta el proyecto?

- Se debe instalar los paquetes del requirements.txt
- Colocar en la consola: 
python manage.py makemigrations
python manage.py migrate 

## APP HOME

# CARPETAS
## views.py

Se crearon las siguientes funciones:
1. cargar_libro:
2. ver_libros:
3. acerca_de_nosotros:
4. index:

## urls.py

- Se crearon los siguientes path:
1. '':
2. 'cargar-libro/':
3. 'ver-libros/':
4. 'Nosotros/':


## models.py

Se creó una clase modelo:
- class Libro:

## forms.py 

En este archivo se encuentra el formulario que tiene Django:
- Para ello tuvimos que importar forms de Django.
- Se creó una clase LibroFormulario que contiene sus siguientes atributos:
nombre, descripcion, categoria, precio y fecha de creacion
- Se creó una clase BusquedaLibroFormulario que contiene como único atributo: nombre. Se utilizará para realizar la busqueda de un libro por su nombre.

## static

Se encuentran los archivos estaticos de css, img, iconos, js.

## templates


