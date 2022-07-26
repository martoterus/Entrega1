from django import forms

class bicisformulario(forms.Form):

    marca = forms.CharField()
    modelo = forms.CharField()
    rodado = forms.CharField()
    color = forms.CharField()
    fecha_fabricacion = forms.DateField()
    precio = forms.IntegerField()

class repuestosFormulario(forms.Form):

    tipo = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    fabricante = forms.CharField()
    fecha_fabricacion = forms.DateField()
    precio = forms.IntegerField()

class indumentariaFormularios(forms.Form):
    tipo = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    talle = forms.CharField()
    precio = forms.IntegerField()