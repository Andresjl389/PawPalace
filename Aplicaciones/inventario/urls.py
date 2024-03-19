from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('indexlibros/', login_required(views.libros, login_url = '/login/'), name = 'libros'),
    path('libroscrear/', login_required(views.crear_libro,login_url='/login/'), name = 'crear_libros'),
    path('libroseditar/', login_required(views.editar_libro, login_url='/login/'), name = 'editar_libros'),
    path('libroseditar/<int:id>', login_required(views.editar_libro, login_url='/login/') , name = 'editar_libros'),
    path('eliminar/<int:id>', login_required(views.eliminar_libro,login_url='/login/'), name = 'eliminar_libros'),

]