from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from django.db import models
from users.models import User
class projectImages(models.Model):
    image = models.ImageField(storage="static/")
    description = models.CharField(max_length=120)

class Tag(models.Model):
    Tag_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.Tag_name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.CharField(max_length=1200, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    owner = models.ForeignKey(User, related_name='owner_of_project', on_delete=models.CASCADE, default=3)
    members = models.ManyToManyField(User, related_name='members_of_project' )
    project_tags = models.ManyToManyField(Tag, default=1, related_name="tags_of_project" )
    github_link = models.CharField(max_length=100, blank=True)
    Live_link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Invite(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    invite_date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, related_name="project_invite", on_delete=models.CASCADE)
    member = models.ForeignKey(User, related_name="invitee", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Invite from {self.project} to {self.member} - {self.status}"