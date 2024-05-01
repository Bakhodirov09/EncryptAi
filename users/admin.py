from django.contrib import admin

from hide_info.models import HiddenInfoModel
from users.models import ConfirmationCodesModel


@admin.register(ConfirmationCodesModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['code', 'email']