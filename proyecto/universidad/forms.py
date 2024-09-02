from django import forms
from .models import Estudiante, Materia, Solicitud
from .validators import validar_cadena_simple, validar_dni, validar_cadena_compuesta

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = "__all__"

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '')
        validar_cadena_simple(nombre, 3, 30)
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido', '')
        validar_cadena_simple(apellido, 3, 30)
        return apellido

    def clean_dni(self):
        dni = self.cleaned_data.get('dni', '')
        validar_dni(dni)
        return dni

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        validar_cadena_compuesta(email, 10, 50)
        return email

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '')
        validar_cadena_compuesta(nombre, 5, 50)
        return nombre

    def clean_turno_de_cursada(self):
        turno_de_cursada = self.cleaned_data.get('turno_de_cursada', '')
        validar_cadena_compuesta(turno_de_cursada, 10, 20)
        return turno_de_cursada

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