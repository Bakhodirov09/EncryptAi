from django.contrib.auth import get_user_model
from django.db import models

from users.models import Base

UsersModel = get_user_model()

class HiddenInfoModel(Base):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='hidden_informations')
    image = models.ImageField(upload_to='hidden_images/', null=True)
    title = models.TextField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Hidden Information'
        verbose_name_plural = 'Hidden Informations'
