from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """Создает и сохраняет пользователя с заданным адресом электронной почты, датой рождения и пароль"""
        if not email:
            raise ValueError('Пользователь должен иметь адрес электронной почты')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    phone = models.CharField(verbose_name='phone number', max_length=12, unique=True, null=True)
    username = models.CharField(verbose_name='username', max_length=20, unique=True)
    avatar = models.ImageField(upload_to='uploads', null=True, blank=True)
    download_avatar = models.FileField(upload_to='uploads', blank=True, null=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    user_admin_description = models.TextField(max_length=255, null=True, blank=True)
    is_verify = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyUserManager()

    def __str__(self):
        return self.email


class VerifyUser(models.Model):
    username = models.CharField(verbose_name='ФИО', max_length=255, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=255, blank=True)
    email = models.EmailField(verbose_name='Почта', max_length=255, blank=True)
    text = models.TextField(verbose_name='О себе', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} {}'.format(self.author, self.phone)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
