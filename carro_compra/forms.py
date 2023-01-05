from django import forms
from inicio.models import electronicomodel

class electronicoform(forms.ModelForm):
    class Meta:
        model = electronicomodel
        fields = ('rating',)


    def clean_rating(self):
        cantidad = self.cleaned_data['rating']    
        articulo = self.cleaned_data['pk']
        articulo = electronicomodel.objects.filter(id=articulo)
        if int(cantidad) < articulo.rating:
            return cantidad    
        
        return self.add_error('no hay esta cantidad')