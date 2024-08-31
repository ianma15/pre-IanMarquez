from django import forms
from .models import Estudiante, Materia, Solicitud

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = "__all__"

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"

class SolicitudForm(forms.ModelForm):
    estudiante = forms.ModelChoiceField(
         queryset=Estudiante.objects.all(), empty_label="Seleccione un estudiante"
    )
    materia = forms.ModelChoiceField(
         queryset = Materia.objects.filter(ofertada=True), empty_label="Seleccione una materia"
    )
    class Meta:
            model = Solicitud
            fields = "__all__"