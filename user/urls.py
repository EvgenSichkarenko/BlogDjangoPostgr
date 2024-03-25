from django import urls
from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]
