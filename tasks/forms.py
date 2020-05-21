from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        task = super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False

    class Meta:
        model = Task
        fields = [
        'name',
        ]