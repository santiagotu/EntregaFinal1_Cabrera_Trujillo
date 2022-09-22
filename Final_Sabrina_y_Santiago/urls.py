from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from accounts.views import login
from Galeria.views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio), 
    path('accounts/', include('accounts.urls')),
    path('Galeria/', include('Galeria.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

