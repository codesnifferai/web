from django import forms
from .models import CodeSnippet

class HomeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))