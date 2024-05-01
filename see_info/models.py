from django.db import models

from hide_info.models import UsersModel
from users.models import Base


class SawInfoModel(Base):
    image = models.ImageField(upload_to='saw_images/', null=True, blank=True)
    title = models.TextField()
    user = models.ForeignKey(UsersModel, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Saw Image'
        verbose_name_plural = 'Saw Images'
