from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('',views.index),
    # path('add/',views.add_person),
    # path('show/',views.get_all_person),
    path('singin/', views.signin, name = 'signin'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.signout, name = 'logout'),
    path('recuperacion/', auth_views.PasswordResetView.as_view(template_name = 'registration/recuperacion.html'), name = 'password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/Confirmacion_Recuperacion.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/CambioContraseña.html'), name = 'password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/Reestablecimiento.html'), name = 'password_reset_complete')
    # path('recuperacion/', views.recuperacion, name = 'recuperacion'),
    # path('password_reset_done/', views.password_reset_done, name = 'password_reset_done'),
    # re_path('(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', views.password_reset_confirm, name = 'password_reset_confirm'),
    # path('password_reset_complete', views.password_reset_complete, name = 'password_reset_complete'),
    # path('inicio/', views.inicio, name = 'inicio'),
] 