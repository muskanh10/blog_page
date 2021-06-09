from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, default="")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    article = models.TextField()

