from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="project/static/img",  allow_folders=True, match="project*", recursive=True)
