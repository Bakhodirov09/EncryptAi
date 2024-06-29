from django.db import models
from django.utils.safestring import mark_safe
from hide_info.models import UsersModel
from users.models import Base

class SawImagesModel(Base):
    user = models.ForeignKey(UsersModel, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=150)
    image = models.ImageField(upload_to='saw_images/', null=True, blank=True)
    decrypted_message = models.TextField()

    def __str__(self):
        return f"{self.decrypted_message[0:len(self.decrypted_message) // 2] if len(self.decrypted_message) > 10 else self.decrypted_message}"

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100px" height="100px" />'.format(self.image.url))

    class Meta:
        verbose_name = 'Saw Image'
        verbose_name_plural = 'Saw Images'

class SawTextsModel(Base):
    user = models.ForeignKey(UsersModel, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=150)
    encrypted_text = models.TextField()
    decrypted_text = models.TextField()

    def __str__(self):
        return f"{self.username}: {self.encrypted_text[0:len(self.decrypted_text) // 2] if len(self.decrypted_text) > 10 else self.decrypted_text}"

    class Meta:
        verbose_name = 'Saw Text'
        verbose_name_plural = 'Saw Texts'
