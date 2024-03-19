from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('info/', views.info, name = 'info'),
    path('quejas/', login_required(views.PQRS, login_url = 'login'), name = 'PQRS'),
]