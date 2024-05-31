from django.db import models
from django.utils import timezone

# Create your models here.

class Document(models.Model):
    documentName = models.CharField(max_length=100, null=False)
    documentPath = models.CharField(max_length=255, null=False)
    createdAt = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.documentName
