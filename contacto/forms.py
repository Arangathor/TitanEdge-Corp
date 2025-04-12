from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(label="Nombre", max_length=15, required=True)
    email = forms.CharField(label="Email", required=True)
    contenido = forms.CharField(label="Mensaje", widget=forms.Textarea)