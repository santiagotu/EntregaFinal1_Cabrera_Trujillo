Proyecto Python Coderhouse 2022.

Grupo: Sabrina Cabrera y Santiago Trujillo Uribe.

Insights del proyecto: https://github.com/santiagotu/EntregaFinal1_Cabrera_Trujillo/graphs/contributors

Instalación: 

1. Crear la base de datos ejecutando:

	>	python manage.py migrate

	>	python manage.py makemigrations

2. Lanzar el servidor web ejecutando:

	> python manage.py runserver

3. Levantado el sitio se debe entrar a la URL generada en la terminal, por defecto: http://127.0.0.1:8000/

Contenido de la Website "Galería de Arte" y Funcionalidades: 

* Registro:
	El usuario tiene que ingresar un usuario, un correo y una contraseña.
	Si no está registrado e intenta logearse, el sistema le avisa que no está registrado.
	Luego de registrarse, el usuario debe ir al link en la navbar de Login y proceder a loguearse.

* Login: 
	El usuario tiene que ingresar su previamente registrado usuario con la contraseña correcta.
	Si la contraseña no es correcta, se le avisa.

* Logout: El usuario se desloguea del sistema y se le da un saludo de despedida.

* Cambio de contraseña.

* Perfil: 
	El usuario puede cambiar sus datos e ingresar un avatar, una descripción y un link.	

* Inicio: página de presentación, se controla a través del login lo que el usuario puede ver y hacer en la web.
	Contiene una barra de navegación superior.

* El proyecto es una app de una Galería de Arte en la cual se puede entrar, mediante un homepage, y navegar por la barra superior por el contenido, según el registro y login previo y realizar ABM de:

	* Artistas: se ingresa el nombre y estilo de un artista. Se puede modificar o borrar el registro.
		Los artistas se visualizan en una página de listado de artistas, en la navbar: Artistas.
	* Obras: se ingresa nombre, fecha, precio, una imagen y se elige un Artista (previamente registrado) de un listado dropdown.
		Las obras se visualizan en una página de listado de obras, en la navbar: Obras.
	* Avaluadores: se ingresa el nombre, la fecha (de avaluación) y una obra (previamente registrada) de un listado dropdown.
		Los avaluadores se visualizan en una página de listado de avaluadores, en la navbar: Avaluadores.

Imagenes extraidas de: https://www.artres.com/

Bootstrap: https://bootstrapmade.com/photofolio-bootstrap-photography-website-template/

Video de navegación de la web:	


