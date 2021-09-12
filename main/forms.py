from .models import Article
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'desription', 'slug']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'placeholder': 'name'}))
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Подтверждение пароль', widget=forms.TextInput(attrs={'placeholder': 'Еще раз'}))
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'placeholder': 'почта'}))


