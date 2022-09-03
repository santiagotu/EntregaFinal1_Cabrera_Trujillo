"""Final_Sabrina_y_Santiago URL Configuration"""

from django.contrib import admin
from django.urls import path, re_path
from Final_Sabrina_y_Santiago import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('inicio/', views.inicio, name="Inicio"),
    path('artistas/', views.artistas, name="Artistas"),
    path('obras/', views.obras, name="Obras"),
    path('avaluadores/', views.avaluadores, name="Avaluadores")

]
