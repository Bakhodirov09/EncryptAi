from django.contrib.auth.models import AbstractUser
from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PromoCodesModel(Base):
    code = models.TextField()
    how_many_times = models.CharField(null=True, blank=True, max_length=20)
    is_active = models.BooleanField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.code} --> {self.how_many_times} --> {self.is_active}"

    class Meta:
        verbose_name = "Promo Code"
        verbose_name_plural = "Promo Codes"

class UsersModel(AbstractUser):
    is_confirmed = models.BooleanField(default=False)
    voice_status = models.BooleanField(default=False)
    voice_date = models.DateField(null=True, blank=True)
    used_promo_codes = models.ManyToManyField(PromoCodesModel, related_name="promo_codes", blank=True)

    def __str__(self):
        return f"{self.get_full_name()}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"



class ConfirmationCodesModel(Base):
    code = models.IntegerField(unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.code}"

    class Meta:
        verbose_name = "Confirmation Code"
        verbose_name_plural = "Confirmation Codes"
