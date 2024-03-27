from django import urls
from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordChangeView

urlpatterns = [
    path('homepage', views.Home.as_view(), name='homepage'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password-change/', views.PasswordChangeUser.as_view(), name='password_change'),
    path('password-change/done/',
         PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"),
         name='password_change_done'),
]
