from django.db import models
from django.utils import timezone

# Create your models here.
class CodeSnippet(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField(null=False)
    source = models.CharField(max_length=60, null=False)
    session_key = models.CharField(max_length=60, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    udpated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'CodeSnippet'
        verbose_name_plural = 'CodeSnippet'
    def __str__(self):
        return self.created_at
class Scores(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    value = models.FloatField(null=False)
    code = models.ForeignKey(CodeSnippet, null=False,  on_delete=models.CASCADE, verbose_name = 'CodeSnippet', related_name='scores',)
    created_at = models.DateTimeField(default=timezone.now)
    udpated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
    def __str__(self):
        return '%s: %s' % (self.name, str(self.value))