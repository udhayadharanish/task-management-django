from django.forms import ModelForm
from .models import Task
from django.forms.widgets import DateTimeInput
from datetime import datetime
from django.forms import DateTimeInput



today = datetime.today()

class TaskForm(ModelForm):
    class Meta:
        model = Task
        
        fields = '__all__'

        widgets = {
            'deadline': DateTimeInput(attrs = {
    'type': 'datetime-local',
    'value': today.strftime('%Y-%m-%dT%H:%M:%S'),
    'min': today.strftime('%Y-%m-%dT%H:%M:%S'),
}),

        }
