from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone_number = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name='страна', blank=True, null=True)
    verification_code = models.CharField(max_length=8, verbose_name='код подтверждения почты', blank=True, null=True)
    is_active = models.BooleanField(default=False, verbose_name='активность')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
