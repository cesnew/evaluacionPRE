from django import forms
from api.models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'edad', 'archivo')


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['nombre', 'fecha_eva', 'fecha_pmyac']

        fecha_eva = forms.DateTimeField(widget=forms.DateInput)
        fecha_pmyac = forms.DateTimeField(widget=forms.DateInput)