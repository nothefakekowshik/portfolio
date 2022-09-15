from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    date = models.DateField()
    url = models.URLField(blank=True)