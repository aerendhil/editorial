from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'appRegistro'

urlpatterns = [
    url('index/', views.index, name = 'index'),
    url('login/', views.usuario_login, name = 'login'),
    url('logout/', views.usuario_logout, name = 'logout'),
    url('registro/', views.registrar, name = 'registro'),
    url('gestionEditorial/', views.gestionarEditorial, name = 'gestionEditorial'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='recuperacion/password_reset_form.html',
             subject_template_name='recuperacion/password_reset_subject.txt',
             email_template_name='recuperacion/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='recuperacion/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='recuperacion/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='recuperacion/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]