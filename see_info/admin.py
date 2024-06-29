from django.contrib import admin

from see_info.models import SawImagesModel, SawTextsModel


@admin.register(SawImagesModel)
class SawImagesAdmin(admin.ModelAdmin):
    list_display = ['admin_photo', 'username']
    search_fields = ['username']
    readonly_fields = ['admin_photo']

@admin.register(SawTextsModel)
class SawTextsAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username', 'decrypted_text', 'encrypted_text']
    list_filter = ['created_at', 'updated_at']
