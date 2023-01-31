from django.conf import settings
from django.db import models
class Certificate(models.Model):
    'Generated Model'
    certificate = models.CharField(max_length=256,)
