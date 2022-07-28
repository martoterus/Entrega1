from django import forms

class bicisformulario(forms.Form):

    Marca = forms.CharField()
    Modelo = forms.CharField()
    Rodado = forms.CharField()
    Color = forms.CharField()
    Precio = forms.IntegerField()

class repuestosFormulario(forms.Form):

    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Fabricante = forms.CharField()
    Precio = forms.IntegerField()

class indumentariaFormularios(forms.Form):
    Tipo = forms.CharField()
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Talle = forms.CharField()
    Precio = forms.IntegerField()