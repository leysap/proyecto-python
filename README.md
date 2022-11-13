![Libros](/home/static/assets/img/biblioteca.jpg)
# **BLOG DE LIBROS**

Proyecto realizado con Python usando Django en el curso de Coderhouse.
Se trata de un blog para poder cargar libros, guardarlos en una base de datos y poder visualizarlos. AsÍ como también, editarlos o eliminarlos.

# **INTEGRANTES**
- Leysa Melina Pozo [Github](https://github.com/leysap)
- Leonardo Bono [Github](https://github.com/leoncio1)
- Julián Gil [Github](https://github.com/AsoreFox)
## ¿Como se levanta el proyecto?

Para este proyecto se creó un entorno virtual. 

En consola:
- Se deben instalar los paquetes del requirements.txt
### pip install -r requirements.txt.
- Siguiente, colocar:
#### python manage.py makemigrations 
#### python manage.py migrate 
#### python manage.py runserver (puerto)

## ***ProyectoDjango***
 
Carpeta que se encuentran las configuraciones del proyecto. En ésta anexamos la aplicación "home", para trabajar nuestras vistas y distintos tipos de pantallas de nuestra web.

# ***APLICACIONES*** 

# **APP HOME**

La creación de esta aplicación nos permite modularizar en "partes".

## *ARCHIVOS - APP HOME*

## models.py

Se creó una clase modelo, para ello importamos models de django.db:

- class Libro: contiene sus siguientes atributos: nombre, escritor, descripcion (utilizando y instalando ckeditor), categoria, precio, fecha de creacion y imagen (se instaló Pillow).
También, en la misma clase se creó una función (magic methods):__str__ , para que se visualice entrando en la base de datos (por admin), el nombre del libro cargado, evitando que se visualice "Libro object".

## forms.py 

En este archivo se encuentra el formulario que tiene Django:

- Para ello tuvimos que importar forms de Django.
- Se creó una clase BusquedaLibroFormulario que contiene como único atributo: nombre. Se utilizará para realizar la búsqueda de un libro por su nombre.

## views.py

### *Vistas basadas en funciones* 
Se crearon las siguientes funciones:

1. ver_libros: función que toma el "nombre" para poder realizar la búsqueda del libro (filtro). Para ello se utilizó la clase BusquedaLibroFormulario (creado en archivo forms.py) para la visualizacion del formulario. Se renderiza este mismo y además se pasa por contexto, los libros creados.
2. acerca_de_nosotros: renderiza template "acerca_de_nosotros.html".
3. index: renderiza el template "index.html".

Para restringir el acceso a mis funciones se aplicó el decorador login_required.
Si el usuario ha iniciado sesión entonces el código de vista se ejecutará como normalmente lo hace. Si el usuario no ha iniciado sesión, se redirigirá al login.

### *Clases Basadas en Vistas (CBV)*

| CBV| Descripcion
   |---|---|
   | CargarLibro | se carga un libro con sus campos/fields de: nombre, descripcion, escritor, categoria, imagen, fecha de creacion y precio.
   | EditarLibro | se edita los datos cargados anteriormente tomando los mismos campos/fields que la clase CargarLibro.
   | EliminarLibro | elimina el libro seleccionado visualizando su template correspondiente para su confirmación.
   | VerLibro | muestra el template ver_libro.html (para visualizar todos los datos cargados de ese libro en particular).

- Todas toman como modelo: Libro.
- El mismo success_url("/ver-libros/" ) para todas las clases.
- Con su template_name correspondiente.

## urls.py

- Se crearon los siguientes path:

1. '': se redirige al index (página principal). Vista basada en función.
2. 'cargar-libro/': se visualiza el formulario para poder cargar un libro a la base de datos. Clase Basada en Vista.
3. 'ver-libros/': se puede visualizar la lista de libros cargados. Vista basada en función.
4. 'nosotros/': breve reseña del equipo del proyecto. Vista basada en función.
5. 'eliminar/< int:pk >': elimina el libro seleccionado. Clase Basada en Vista.
6. 'ver_libro/ < int:pk >': muestra el libro con mayor información. Clase Basada en Vista.
7. 'editar/< int:pk >': muestra su template para poder editar la información de ese libro en particular. Clase Basada en Vista.
 

## >>> *CARPETAS - APP HOME*
## static

Se encuentran los archivos estáticos de css, img, iconos, js.
- Para el header agregamos una imagen en representación de nuestro blog de libros.

## templates

1. Se utilizó una plantilla traido de Start Bootstrap.
2. Se realizó herencia de templates utilizando un solo archivo como base para el resto.

Los archivos templates creados son:

- base.html: archivo base, se encuentran las etiquetas html, head, body (dentro de éste: nav, footer y los scripts de js). En la etiqueta nav se crearon enlaces directos para cada template. Además, se usó los "block" para que el resto (templates) pueda cargar su contenido. También, se encuentra los enlaces de iniciar sesion, cerrar sesion y de registrarse.
- acerca_de_nosotros.html: siemple vista que contiene una breve reseña del equipo.
- cargar_libro.html: Se agrego una pantalla que permite la carga de los libros a nuestra base de datos, utilizando la clase y la tabla previamente creada.
- index.html: Se usa como pantalla principal de nuestro proyecto.
- ver_libros.html: Se muestra el listado de libros creados. Con su nombre y el escritor. En este mismo se encuentra el buscador de libro por su nombre. Si no lo encuentra, se muestra un mensaje de no hay resultados. Además, se muestra el autor del posteo(tomando el nombre del usuario que se ha registrado).
- ver_libro.html: Se muestra el libro de manera independiente con los siguientes datos: nombre, escritor, descripcion, categoria, precio, fecha de creacion y imagen.
- eliminar_libro.html: En este template se confirma el borrado del libro.
- editar_libro.html: muestra el formulario con los datos cargados anteriormente para poder editarlos.

# **APP ACCOUNTS**

Esta aplicación se creó para el login/logout y registro.

## >> *ARCHIVOS - APP ACCOUNTS*

## models.py

- ExtensionUsuario: utiliza campos de: avatar(ImageField), web(Charfield) y user(OneToOneField).
Este modelo se relaciona con el usuario.
También en la misma clase, se creó una función (magic methods):__str__ , para que se visualice entrando en la base de datos (por admin) el nombre del usuario.

Para el avatar se tuvo que instalar Pillow. Para este campo se indicó a qué carpeta se van a guardar las imágenes (upload_to='avatares'). 


## forms.py 

- MiFormularioDeCreacion: en esta clase se crea un formulario para utilizarlo en el registro. Tiene de campos: 'email,  password1, password2'. Dentro de esta clase se agregó un class Meta (identifica ciertos valores que va a tener el formulario como configuraciones).
- EditarPerfilFormulario: se crea un formulario para editar los datos del perfil. Tiene de campos: 'email, first_name, last_name, avatar, web'.
- MiCambioDeContrasenia: hereda de el PasswordChangeForm. Se utiliza de campos: 'old_password, new_password1 y new_password2'. Dentro de esta clase tambien se agregó un class Meta.

## urls.py 
Se encuentran los siguientes path:

- path('login/') Vista basada en función.
- 'registrar/' Vista basada en función.
- 'logout/' Clase Basada en Vista (CBV). 
- 'perfil/' Vista basada en función.
- 'perfil/editar/' Vista basada en función.
- 'perfil/cambiar-contrasenia/' Clase Basada en Vista (CBV).

## views.py

### *Vistas basadas en funciones*
- mi_login: en esta función se utiliza el formulario que nos brinda Django, con el AuthenticationForm y login. Permite loguearse. Una vez logueado, redirige al index.
- registrar: como su nombre lo indica, permite registrarse utilizando MiFormularioDeCreacion (creado en forms.py).
- perfil: renderiza su correspondiente template('perfil'), mostrando información del usuario logueado. Se utilizó en esta función el decorador login_required.
- editar_perfil: utiliza EditarPerfilFormulario (en forms.py) y ExtensionUsuario (models.py) para poder editar los datos del perfil: 'email, nombre, apellido, avatar, web'.

Se utilizó el decorador login_required para restringir el acceso a nuestras funciones, usuarios que no están logueados.

### *Clases Basadas en Vistas*

- class CambiarContrasenia: esta clase hereda de la vista PasswordChangeView. Utiliza un template_name (cambiar_contrasenia), un success_url (se coloca una url, template a donde se va a redirigir luego de cambiar la contraseña) y un form_class(MiCambioDeContrasenia).

Se utilizó para esta clase, el mixin LoginRequiredMixin, que nos va permitir limitar a un usuario que no esta logueado para poder acceder a una parte de nuestra página. 

## >> *CARPETAS - APP ACCOUNTS*

## templates 

- login.html: muestra el formulario de login,(el que nos brinda Django) con su usuario y contraseña.
- logout.html: se creo una CBV desde el urls.py trayendo desde django a LogoutView. En este template confirma el cerrado de sesion.
- registrar.html: muestra el formulario creado (de MiFormularioDeCreacion) que permite registrarse con sus campos de 'email, contraseña y repetir contraseña'.
- perfil.html: muestra información del usuario logueado. Con su avatar, nombre, apellido, email y link a una página (web). Se agregó tambien dos enlaces: 1. para editar datos del perfil, 2. para cambiar la contraseña.
- editar_perfil.html: muestra el formulario creado (de EditarPerfilFormulario).
- cambiar_contrasenia.html: muestra el formulario (de la CBV CambiarContrasenia) para cambiar la constraseña.


