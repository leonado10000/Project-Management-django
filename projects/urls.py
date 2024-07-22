from django.urls import path, include
from .views import project_list, project_detail, project_create,project_update
from .views import *

urlpatterns = [
    path('', project_list, name='my_projects'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/update/', project_update, name='project_update'),
    path('my_invites/', invites_page, name='invites_page'),
    path('<int:pk>/invites/', invite_user, name='invite_user'),
    path('invites/', invite_user2, name='invite_user2'),
    path('invites/handle/', handle_invite, name='handle_invite'),
]