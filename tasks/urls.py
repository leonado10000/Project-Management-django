from django.urls import path
from .views import task_list, task_detail, task_form, task_delete

urlpatterns = [
    path('project/<int:project_id>/', task_list, name='task_list'),
    path('project/<int:project_id>/create/', task_form, name='task_create'),
    path('project/<int:project_id>/task/<int:pk>/', task_detail, name='task_detail'),
    path('project/<int:project_id>/task/<int:pk>/update/', task_form, name='task_update'),
    path('project/<int:project_id>/task/<int:pk>/delete/', task_delete, name='task_delete'),
]
