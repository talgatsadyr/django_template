from django.db import models


class UserStatusChoices(models.TextChoices):
    simple = 'simple', 'Простой'
    VIP = 'VIP', 'ВИП'
