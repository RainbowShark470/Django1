from django.db import models

# Create your models here.
class Blog(models.Model):
    blog.title = models.CharField(max_length=275)
    blog.description = models.CharField(max_length=1025)
    blog.owner = models.CharField(max_length=275)