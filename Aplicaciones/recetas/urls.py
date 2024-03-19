from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('recetas/', login_required(views.recetas, login_url = "/login/"), name = 'recetas'),
    path('info_receta/<str:Nombre_receta>/', login_required(views.info_recetas, login_url = "/login/"), name = 'Rece_Info'),

]