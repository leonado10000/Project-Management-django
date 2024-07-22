from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'members']
        widgets = {
          'description': forms.Textarea(attrs={'rows':7, 'cols':50}),
        }