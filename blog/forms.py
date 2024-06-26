from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import EmailSubs, Comments


class Register(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class EmailSubsForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'type': 'search',
        'placeholder': 'Email'
    }))

    class Meta:
        model = EmailSubs
        fields = ('email',)


class CommentsForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'search',
        'placeholder': 'Your name',
        'style': 'margin-bottom:10px'
    }))
    context = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'search',
        'placeholder': 'Message',
        'style': 'margin-bottom:10px'
    }))

    class Meta:
        model = Comments
        fields = ('username', 'context')
