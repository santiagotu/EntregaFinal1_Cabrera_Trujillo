from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include
from accounts.views import login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('inicio/', admin.site.urls),
    path('', lambda req: redirect('inicio')),
    path('Galeria/', include('Galeria.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

