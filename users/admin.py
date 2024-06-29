from django.contrib import admin
from users.models import ConfirmationCodesModel, UsersModel


@admin.register(UsersModel)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_active', 'voice_status']
    search_fields = ['username', 'first_name', 'last_name', 'email']

@admin.register(ConfirmationCodesModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['code', 'email']