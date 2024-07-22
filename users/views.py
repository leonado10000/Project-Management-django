from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.contrib.auth import authenticate


def register(request):
    print("it came here")
    if request.method == 'POST':
        print("seomething",request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

class ProjectListView(TemplateView):
    template_name = 'project_list.html'

class UserRegisterView(TemplateView):
    template_name = 'register.html'

class UserLoginView(LoginView):
    template_name = 'login.html'

class UserLogoutView(LogoutView):
    template_name = 'logout.html'

class UserSettingsView(TemplateView):
    template_name = 'settings.html'

class UserRoleView(TemplateView):
    template_name = 'role.html'