from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        labels = {
            'title': 'Title', 
            'description': 'Description',
            'due_date': 'Due Date'
        }
        widgets = {
            'description': forms.Textarea(),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }