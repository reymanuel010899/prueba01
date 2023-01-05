from django import forms
from .models import electronicomodel

class electronicoform(forms.ModelForm):
    class Meta:
        model = electronicomodel
        fields = ('rating',)

    def clean_rating(self):
        cantidad = self.cleaned_data['rating']    
        articulo = self.cleaned_data['pk']
        articulo = electronicomodel.objects.filter(id=articulo)
        if cantidad > articulo.rating:
            raise forms.ValidationError('no hay esta cantidad')
        return cantidad    
