from django.contrib import admin

from hide_info.models import HiddenInfoModel


@admin.register(HiddenInfoModel)
class HiddenInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['id', 'title', 'user']
    list_filter = ['created_at', 'updated_at']