"""
URL configuration for food_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from .views import suscripcion, principal, comunidad, inicio
from .views import inicio,  suscripcion, principal, padmin
from django.contrib.auth.decorators import login_required

from django.urls import re_path
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', login_required(inicio, login_url = "/login/"), name = 'inicio'),
    path('suscripcion/', login_required(suscripcion, login_url = "/login/"), name = 'suscripcion'),
    path('padmin/', login_required(padmin, login_url='/login/') , name = 'perfil_administrativo'),
    path('', principal, name = 'principal'),
    path('', include('Aplicaciones.Conexion.urls')),
    path('', include('Aplicaciones.recetas.urls')),
    path('', include('Aplicaciones.contacto.urls')),
    path('', include('Aplicaciones.inventario.urls')),
    path('', include('Aplicaciones.apiproductost.urls')),
    path('', include('Aplicaciones.Comunidad.urls')),
    path('', include('Aplicaciones.Admin.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    
]
