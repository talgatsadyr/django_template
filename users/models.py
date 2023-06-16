from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from users.choices import UserStatusChoices


class UserManager(BaseUserManager):
    def create_user(self, password, email, **extra_fields):
        user = self.model(**extra_fields)
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, email, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(password, email, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='profile/images/', verbose_name='Аватар', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_status = models.CharField(max_length=255, blank=True, choices=UserStatusChoices.choices,
                                   default=UserStatusChoices.simple)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'
