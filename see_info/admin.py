from django.contrib import admin

from see_info.models import SawInfoModel


@admin.register(SawInfoModel)
class SawInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at', 'title']
    search_fields = ['id', 'title']
    list_filter = ['created_at', 'updated_at']
