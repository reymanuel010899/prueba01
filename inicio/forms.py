from django import forms
from .models import electronicomodel

class electronicoform(forms.ModelForm):
    class Meta:
        model = electronicomodel
        fields = ('rating',)