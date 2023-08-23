from django.contrib import admin

# Register your models here.

from .models import CodeSnippet

admin.site.register(CodeSnippet)