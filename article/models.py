from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    ENABLED = 'en'
    DISABLED = 'ds'
    status_choices =[(ENABLED,'Enabled'),(DISABLED),('Disabled')]
    title = models.CharField(max_length=255)
    brief = models.CharField(max_length=300)
    content = models.TextField()
    main_image = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    status = models.CharField(max_length=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)