from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Project)
admin.site.register(models.projectImages)
admin.site.register(models.Tag)

admin.site.register(models.Invite)