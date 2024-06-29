from django.contrib import admin

from hide_info.models import HiddenImagesModel, HiddenTextsModel


@admin.register(HiddenImagesModel)
class HiddenImagesModelAdmin(admin.ModelAdmin):
    list_display = ['admin_photo', 'username']
    search_fields = ['title', 'username']
    readonly_fields = ['admin_photo']

@admin.register(HiddenTextsModel)
class HiddenTextsModelAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username', 'decrypted_text', 'encrypted_text']
    list_filter = ['created_at', 'updated_at']