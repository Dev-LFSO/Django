from django.forms import ModelForm
from .models import Sala

class SalaForm(ModelForm):
    class Meta:
        model = Sala
        fields = '__all__'