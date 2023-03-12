from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Status(models.IntegerChoices):
        active = 1, 'Active'
        archived = 2, 'Archived'

    username = models.CharField(max_length=25, unique=True)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.active)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
