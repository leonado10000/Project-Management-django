from django.urls import path, include
from .views import *
from projects.views import invites_page
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('settings/', UserSettingsView.as_view(), name='settings'),
]
