from django.urls import path, include

from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('see-info/', include('see_info.urls', namespace='see_info')),
    path('hide-info/', include('hide_info.urls', namespace='hide_info'))
]
