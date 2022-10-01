from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Galeria import views
from Galeria.views import inicio, acerca_de_nosotros, paginas   
from accounts.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('about', acerca_de_nosotros, name='acerca_de_nosotros'),
    path('accounts/', include('accounts.urls')),
    path('pages/', paginas, name = 'paginas'),
    
    path('crear_artistas/', views.CrearArtista.as_view(), name='crear_artistas'),
    path('listado_artistas/', views.ListadoArtistas.as_view(), name='listado_artistas'),
    path('editar_artista/<int:pk>', views.EditarArtista.as_view(), name='editar_artista'),
    path('eliminar_artista/<int:pk>', views.EliminarArtista.as_view(), name='eliminar_artista'),    

    path('crear_obras/', views.CrearObra.as_view(), name='crear_obras'),
    path('listado_obras/', views.ListadoObras.as_view(), name='listado_obras'),
    path('editar_obra/<int:pk>', views.EditarObra.as_view(), name='editar_obra'),
    path('eliminar_obra/<int:pk>', views.EliminarObra.as_view(), name='eliminar_obra'),  

    path('crear_avaluadores/', views.CrearAvaluador.as_view(), name='crear_avaluadores'),
    path('listado_avaluadores/', views.ListadoAvaluadores.as_view(), name='listado_avaluadores'),
    path('editar_avaluador/<int:pk>', views.EditarAvaluador.as_view(), name='editar_avaluador'),
    path('eliminar_avaluador/<int:pk>', views.EliminarAvaluador.as_view(), name='eliminar_avaluador'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

