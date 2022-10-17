# BLOG DE LIBROS

Proyecto realizado con Python usando Django en el curso de Coderhouse.
Se trata de un blog para poder cargar libros, guardarlos en una base de datos y poder visualizarlos.

## ¿Como se levanta el proyecto?

Para este proyecto se creó un entorno virtual.

- Se deben instalar los paquetes del requirements.txt
- Colocar en la consola: 
#### python manage.py makemigrations 
#### python manage.py migrate 
#### python manage.py runserver (puerto)

## ProyectoDjango
 
Carpeta que se encuentran las configuraciones del proyecto. En ésta anexamos la aplicación "home".

## APP HOME

La creación de esta aplicación nos permite modularizar en "partes".

# CARPETAS

## views.py

Se crearon las siguientes funciones:

1. cargar_libro: función que toma los datos colocados en el formulario (creado por la clase LibroFormulario en el archivo forms.py), realiza su validación por metodo "POST" y los guarda en la base de datos. Al cargar uno, se redirige al template "ver_libros.html" para visualizar el listado de libros creados.
2. ver_libros: función que toma el "nombre" para poder realizar la búsqueda del libro (filtro). Para ello se utilizó la clase BusquedaLibroFormulario (creado en archivo forms.py) para la visualizacion del formulario. Se renderiza este mismo y además se pasa por contexto, los libros creados.
3. acerca_de_nosotros: renderiza template "acerca_de_nosotros.html".
4. index: renderiza el template "index.html".

## urls.py

- Se crearon los siguientes path:

1. '': se redirige al index (página principal).
2. 'cargar-libro/': se visualiza el formulario para poder cargar un libro a la base de datos.
3. 'ver-libros/': se puede visualizar la lista de libros cargados.
4. 'nosotros/': breve reseña del equipo del proyecto.

## models.py

Se creó una clase modelo, para ello importamos models de django.db:

- class Libro: contiene sus siguientes atributos: nombre, descripcion, categoria, precio y su fecha de creacion. 
También, en la misma clase se creó una función (magic methods):__str__ , para que se visualice entrando en la base de datos (por admin), el nombre del libro cargado, evitando que se visualice "Libro object".

## forms.py 

En este archivo se encuentra el formulario que tiene Django:

- Para ello tuvimos que importar forms de Django.
- Se creó una clase LibroFormulario que contiene sus siguientes atributos:
nombre, descripcion, categoria, precio y fecha de creacion
- Se creó una clase BusquedaLibroFormulario que contiene como único atributo: nombre. Se utilizará para realizar la búsqueda de un libro por su nombre. 

## static

Se encuentran los archivos estáticos de css, img, iconos, js.
- Para el header agregamos una imagen en representación de nuestro blog de libros.

## templates

1. Se utilizó una plantilla traido de Start Bootstrap.
2. Se realizó herencia de templates utilizando un solo archivo como base para el resto.

Los archivos templates creados son:

- base.html: archivo base, se encuentran las etiquetas html, head, body (dentro de éste: nav, footer y los scripts de js). En la etiqueta nav se crearon enlaces directos para cada template. Además, se usó los "block" para que el resto (templates) pueda cargar su contenido. 
- acerca_de_nosotros.html: siemple vista que contiene una breve reseña del equipo.
- cargar_libro.html: visualiza el formulario para cargar un libro.
- index.html: se encuentra el header.
- ver_libros.html: Se muestra el listado de libros creados.En este mismo se encuentra el buscador de libro por su nombre. Si no lo encuentra, se muestra un mensaje. 
