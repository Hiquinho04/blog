from django import forms
from .models import Title

class NewTopic(forms.ModelForm):
    """Forms for new topics"""
    class Meta:
        model = Title
        fields = ['title']
        labels = {'title': ''}