from django.urls import path
from . import views


urlpatterns = [
    path('comunidad/', views.comentar, name = 'comenComunidad'),
    path('respuesta/', views.rta, name = 'Respuesta'),

]