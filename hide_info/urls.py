from django.urls import path

from dashboard.views import HideInfoView
from hide_info.views import *

app_name = 'hide_info'

urlpatterns = [
    path('', HideInfoView.as_view(), name='hide_info'),
    path('with-photo/', HideInfoWithPhotoView.as_view(), name='with_photo'),
    path('with-text/', HideInfoWithTextView.as_view(), name='with_text')
]
