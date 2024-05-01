from django.urls import path

from dashboard.views import *
from see_info.views import SeeInfoWithImageView, SeeInfoWithTextView

app_name = 'see_info'

urlpatterns = [
    path('', SeeInfoView.as_view(), name='see_info'),
    path('with-photo/', SeeInfoWithImageView.as_view(), name='with_photo'),
    path('with-text/', SeeInfoWithTextView.as_view(), name='with_text')
]