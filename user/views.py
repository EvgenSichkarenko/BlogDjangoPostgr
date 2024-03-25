from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import Register, Login


# Create your views here.
class RegisterUser(CreateView):
    template_name = 'user/register.html'
    form_class = Register
    success_url = reverse_lazy('home')


class LoginUser(LoginView):
    form_class = Login
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')



