from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import LoginView, RegisterView, AccountView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/', AccountView.as_view(), name='logout'),
    path('activating/gmail=<str:gmail>/', LoginView.as_view(), name='activate'),
]