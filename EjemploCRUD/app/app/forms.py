from django import forms

class FormPersona(forms.Form):
    rut = forms.CharField(max_length=13, required=True)
    nombre = forms.CharField(max_length=15, required=True)
    apellidos = forms.CharField(max_length=20, required=True)
    direccion = forms.CharField(max_length=50, required=True)
    correo_electronico = forms.EmailField(max_length=70, required=True)
    fecha_nacimiento = forms.DateField()

    