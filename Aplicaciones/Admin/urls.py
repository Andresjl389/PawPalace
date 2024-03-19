from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('adm_recetas/', login_required(views.vista_recetas, login_url = "/login/"), name = 'adm_recetas'),
    path('crear_receta/', login_required(views.crear_receta, login_url = "/login/"), name = 'crear_recetas'),
    path('eliminar_receta/<int:id>/', login_required(views.eliminar_receta, login_url = "/login/"), name = 'eliminar_recetas'),
    path('editar_receta/<int:id>/', login_required(views.editar_receta, login_url = "/login/"), name = 'editar_recetas'),

]