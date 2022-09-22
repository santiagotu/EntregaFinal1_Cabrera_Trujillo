from django.contrib import admin
from django.urls import path
from .views import login, register, perfil, editar_perfil, ChangePasswordView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    #path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('cambiar_password/', ChangePasswordView.as_view(), name='cambiar_password')


]