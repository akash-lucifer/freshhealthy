from django.db import models
from django.conf import settings

from django.utils import timezone
# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=64, null=True)  # works
    language_code = models.CharField(max_length=2, default='en')  # works
    #is_dumb = models.BooleanField(default=False),  # doesn't work
