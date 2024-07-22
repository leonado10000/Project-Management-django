# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Invite, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from users.models import User
from django.http import JsonResponse
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project = pk).all()
    return render(request, 'project_detail.html', {'project': project, 'tasks': tasks })

@login_required
def project_create(request):
    tags = Tag.objects.all()
    u = request.user
    if request.method == 'POST':
        data = request.POST
        print(data)
        print(User.objects.get(pk = int(data['owner'])))
        print([Tag.objects.get(pk = int(t)) for t in data['project_tags']])
        p = Project(
            name = data['name'],
            description = data['description'],
            features = data['features'],
            start_date = data['start_date'],
            end_date = data['end_date'],
            github_link = data['github_link'],
            Live_link = data['live_link'],
            owner = User.objects.get(pk = int(data['owner']))
        )
        p.save()
        p.project_tags.set([Tag.objects.get(pk = int(t)) for t in data['project_tags']] )
        p.save()
        print(p)
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form, "tags":tags, "user":u})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_update_form.html', {'form': form, 'project': project})

def showimages(request):
    return render(request, 'images.html')


@login_required
def invite_user(request, pk):
    if request.method == 'POST':
        member_id = request.POST.get('username')
        member = get_object_or_404(User, username=member_id)
        p = Project.objects.filter(pk = pk)[0]
        invite = Invite(project=p, member=member)
        invite.save()
        return JsonResponse({'status': 'Invite sent successfully'})
    
@login_required
def invite_user2(request):
    if request.method == 'POST':
        project_id = request.POST.get('project-id')[0]
        member = request.POST.get('username')
        print("got request")
        member = get_object_or_404(User, username=member)
        p = Project.objects.get(pk = int(project_id))
        invite = Invite(project=p, member=member)
        print("careted invite", invite)
        invite.save()
        response_data = {
                'message': 'Success',
                'project_id': project_id,
                'member_id': member.id,
            }
        return JsonResponse(response_data)
    return redirect('invites_page')

@login_required
def handle_invite(request):
    if request.method == "POST":
        action = request.POST.get('invite_action')
        invite_id = request.POST.get("invite_id")
        print("request came to ",action,invite_id)
        invite = get_object_or_404(Invite, id=invite_id)
        if request.user != invite.member:
            return JsonResponse({'status': 'You do not have permission to perform this action'}, status=403)
        
        if action == 'accept':
            invite.status = 'accepted'
            p = Project.objects.get(pk = invite.project.id)
            p.members.add(invite.member.id)
            p.save()
        elif action == 'reject':    
            invite.status = 'rejected'
        
        invite.save()
        return JsonResponse({'status': f'Invite {action}ed successfully'})



@login_required
def invites_page(request):
    your_projects = Project.objects.filter(owner = request.user)
    your_invites = Invite.objects.filter(member=request.user)
    sent_invites = []
    for projects_ in your_projects:
        for inv in Invite.objects.filter(project = projects_):
            sent_invites.append(inv)
    return render(request, 'invites_page.html', {"projects":your_projects,'invites': your_invites, 'sent_invites': sent_invites})
