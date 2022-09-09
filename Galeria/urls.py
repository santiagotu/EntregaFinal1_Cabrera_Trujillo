from django.contrib import admin
from django.urls import path, include
from Galeria import views

app_name = "Galeria"
urlpatterns = [
    path('admin', admin.site.urls), 
    path('', views.inicio, name='inicio'),
    path('artistas', views.artista, name="artista"),
    path('avaluadores', views.avaluador, name="avaluador"),
    path('obras', views.obras, name="obras"),
    path('buscar/', views.buscar),

]