from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    #path('inicio/', admin.site.urls),
    path('', lambda req: redirect('inicio')),
    path('Galeria/', include('Galeria.urls')),
=======
    path('admin/', admin.site.urls),
    #path('', lambda req: redirect('inicio')),
    path('', include('Galeria.urls')),
>>>>>>> 9e4c7a09715f87ce07c933d3d5171a0a283a5429

]

