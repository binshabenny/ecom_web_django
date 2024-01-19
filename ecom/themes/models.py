from django.db import models

# Create your models here.
class SlideSettings(models.Model):
    banner = models.ImageField(upload_to='banner/')
    caption = models.TextField()
