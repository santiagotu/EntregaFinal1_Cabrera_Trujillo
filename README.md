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

Funcionalidades: 

El proyecto es una app de una Galería de Arte en la cual se puede entrar, mediante un homepage, y
visualizar y realizar AMB de:

	* Artistas	
	* Obras	
	* Avaluadores

Contenido de la website:

* Registro:
	El usuario tiene que ingresar un usuario, un correo y una contraseña.
	Si no está registrado e intenta logearse, el sistema le avisa que no está registrado.

* Login: 
	El usuario tiene que ingresar su previamente registrado usuario con la contraseña correcta.
	Si la contraseña no es correcta, se le avisa.

* Logout: El usuario se desloguea del sistema y se le da un saludo de despedida.

* Cambio de contraseña.

* Perfil: 
	El usuario puede cambiar sus datos e ingresar un avatar.	

* Inicio: página de presentación, se controla a través del login lo que el usuario puede ver y hacer en la web.
	Contiene una barra de navegación superior

* ABM de Artistas, Obras y Avaluadores.

Imagenes extraidas de: https://www.artres.com/
Bootstrap: https://bootstrapmade.com/photofolio-bootstrap-photography-website-template/

Video de navegación de la web:	


