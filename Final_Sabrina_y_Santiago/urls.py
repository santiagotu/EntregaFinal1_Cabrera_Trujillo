from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('inicio/', admin.site.urls),
    #path('', lambda req: redirect('inicio')),
    path('Galeria/', include('Galeria.urls')),

]

