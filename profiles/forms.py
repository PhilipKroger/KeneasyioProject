from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from .models import *

from ckeditor.widgets import CKEditorWidget

User = get_user_model()


class UserLoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'login_email_form', 'id': 'login_form_email_label'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'login_password_form', 'id': 'login_form_password_label'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('This user does not exist!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Wrong password!')
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Account disabled')
        return super(UserLoginForm, self).clean()


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(label="Почта",
                            widget=forms.EmailInput(
                                attrs={'class': 'register_email_form', 'id': 'register_form_email_label'}))
    phone = forms.CharField(label="Телефон",
                            widget=forms.TextInput(
                                attrs={'class': 'register_phone_form', 'id': 'register_form_phone_label'}))
    username = forms.CharField(label="Имя",
                               widget=forms.TextInput(
                                   attrs={'class': 'register_username_form', 'id': 'register_form_username_label'}))
    description = forms.CharField(label="Описание профиля",
                                  widget=forms.TextInput(attrs={'class': 'register_description_form',
                                                                'id': 'register_form_description_label'}))
    avatar = forms.ImageField(label='Фото вашего профиля')
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(
                                   attrs={'class': 'register_password_form', 'id': 'register_form_password_label'}))
    password2 = forms.CharField(label="Подтвержите пароль",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'register_password2_form', 'id': 'register_form_password2_label'}))

    class Meta:
        model = User
        fields = ('email', 'phone', 'username', 'avatar', 'password', 'password2')

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError('Email is taken!')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords do not match")
        return data["password2"]


class VerifyForm(forms.ModelForm):
    username = forms.CharField(label='Введите ФИО', max_length=255)
    phone = forms.CharField(label='Введите ваш номер телефона', max_length=255)
    email = forms.EmailField(label='Ваша почта')
    text = forms.CharField(
        label='Расскажите о себе (Ваш опыт, навыки, достижения и тд)',
        widget=CKEditorWidget(
            attrs={
                'class': 'product_form_text',
                'id': 'product_form_text_label'
            }
        )
    )

    class Meta:
        model = VerifyUser
        fields = ('username', 'phone', 'email', 'text')
