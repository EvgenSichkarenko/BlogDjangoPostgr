from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from user.forms import Register, Login, PasswordChange
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User


# Create your views here.
class RegisterUser(CreateView):
    template_name = 'user/register.html'
    form_class = Register
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # save the new user first
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url)


class LoginUser(LoginView):
    form_class = Login
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')


class PasswordChangeUser(PasswordChangeView):
    form_class = PasswordChange
    success_url = reverse_lazy("password_change_done")
    template_name = "user/password_change.html"


class Home(View):
    def get(self, request):

        users = User.objects.all()

        context = {
            'users': users
        }

        return render(request, 'user/home_pg.html', context)
