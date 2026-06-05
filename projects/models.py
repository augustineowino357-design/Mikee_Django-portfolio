from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50) # e.g. "Django, Bootstrap"
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
