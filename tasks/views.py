from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from users.models import User
from projects.models import *
from .forms import TaskForm
from projects.models import Project

def task_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project = project_id).all()
    return render(request, 'task_list.html', {'project': project, 'tasks': tasks})

def task_detail(request,project_id, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_form(request, project_id, pk=None):
    project = get_object_or_404(Project, id=project_id)
    if pk:
        task = get_object_or_404(Task, pk=pk)
    else:
        task = None
    if request.method == 'POST':
        data = request.POST
        t = Task(
            name = data['tname'],
            description = data['tdesc'],
            due_date = data['Due_date'],
            status = data['status'],
            assigned_to = User.objects.get(pk = int(data['assign_to'])),
            project = Project.objects.get(pk = project_id)
            )
        t.save()
        form = TaskForm(request.POST, instance=task)
        return redirect("project_detail",project_id)
    else:
        form = TaskForm(instance=task)
    
    task_choices = Task.STATUS_CHOICES
    return render(request, 'task_form.html', {'form': form, 'task': task, "project":project, "task_choices": task_choices})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project_id = task.project.id
    task.delete()
    return redirect('task_list', project_id=project_id)
