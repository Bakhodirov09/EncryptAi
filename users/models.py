from django.contrib.auth.models import AbstractUser
from django.db import models

from users.form import UsersModel


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ConfirmationCodesModel(Base):
    code = models.IntegerField(unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.code}"

    class Meta:
        verbose_name = "Confirmation Code"
        verbose_name_plural = "Confirmation Codes"
