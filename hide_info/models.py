from django.db import models
from django.utils.safestring import mark_safe
from users.models import Base, UsersModel

class HiddenImagesModel(Base):
    user = models.ForeignKey(UsersModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='hidden_images')
    username = models.CharField(max_length=150)
    image = models.ImageField(upload_to='hidden_images/')
    title = models.TextField()

    def __str__(self):
        return self.title

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100px" height="100px" />'.format(self.image.url))

    admin_photo.short_description = 'Image'

class HiddenTextsModel(Base):
    user = models.ForeignKey(UsersModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='hidden_texts')
    username = models.CharField(max_length=150)
    encrypted_text = models.TextField()
    decrypted_text = models.TextField()

    def __str__(self):
        return self.decrypted_text[:len(self.encrypted_text) // 2]

    class Meta:
        verbose_name = 'Hidden Text'
        verbose_name_plural = 'Hidden Texts'
