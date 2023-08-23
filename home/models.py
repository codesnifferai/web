from django.db import models

# Create your models here.
class CodeSnippet(models.Model):
    code = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField("date created")


