from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('inicio/', admin.site.urls),
    path('Galeria/', include('Galeria.urls')),

]

