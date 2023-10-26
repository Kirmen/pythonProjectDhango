from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
import re

from .models import Bags


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
    captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Им\'я користувача', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # username = forms.CharField(label='Ім\'я користувача', help_text='Максимум 150 символів',
    #                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(label='Підтвердження паролю',
    #                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class BagsForm(forms.ModelForm):
    class Meta:
        model = Bags
        # fields = '__all__'
        fields = ['title', 'description', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Назва не повинна починатись з цифри')
        return title

    # title = forms.CharField(max_length=150, label="Бренд:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(label='Опис:', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 5}))
    # is_published = forms.BooleanField(label='Опубліковано:', initial=True)
    # category = forms.ModelChoiceField(empty_label='Оберіть категорію', queryset=Category.objects.all(),
    #                                   label='Категорія:', widget=forms.Select(attrs={'class': 'form-control'}))
