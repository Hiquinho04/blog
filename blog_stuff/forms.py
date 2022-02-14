from django import forms
from .models import Title, Text

class NewTopic(forms.ModelForm):
    """Forms for new topics"""
    class Meta:
        model = Title
        fields = ['title']
        labels = {'title': ''}

class New_Entry(forms.ModelForm):
    """Forms for new entry"""
    class Meta:
        model = Text
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}