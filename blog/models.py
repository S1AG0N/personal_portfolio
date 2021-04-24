from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField('date published')
    script = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='blogs/images/', default='')

    def __str__(self):
        return self.title




