from django import forms
from .models import TaskModel

#Task Form
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = [
            'title',
            'description',
            'completed'
            # 'created_at'
        ]
