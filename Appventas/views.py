
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from Appventas.models import bicicletas
from Appventas.forms import bicisformulario
from Appventas.forms import repuestosFormulario
from Appventas.models import repuestos
from Appventas.forms import indumentariaFormularios
from Appventas.models import indumentaria
# Create your views here.


def inicio(request):

    return render(request, "inicio.html")

def tablabici(request):

    return render(request, "tablabici.html")


def bicis(request):

    if request.method == 'POST':

        miFormulario = bicisformulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            bici = bicicletas(marca = informacion["marca"], modelo = informacion["modelo"], rodado = informacion["rodado"], color = informacion["color"], fecha_fabricacion = informacion["fecha_fabricacion"], precio = informacion["precio"])
            
            bici.save()

            return render(request, "inicio.html")

    else:
        miFormulario = bicisformulario()

        return render(request, "tablabici.html", {"miFormulario":miFormulario})
        

def repuesto(request):

    if request.method == 'POST':

        miFormulario = repuestosFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            rep = repuestos(tipo = informacion["tipo"], marca = informacion["marca"], modelo = informacion["modelo"], fabricante = informacion["fabricante"], fecha_fabricacion = informacion["fecha_fabricacion"], precio = informacion["precio"])
            
            rep.save()

            return render(request, "Appventas/inicio.html")

        else:
            miFormulario = repuestosFormulario()

        return render(request, "Appventas/repuestosformulario.html", {"miFormulario":miFormulario})


def indumentarias(request):

    if request.method == 'POST':

        miFormulario = indumentariaFormularios(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            indum = indumentaria(tipo = informacion["tipo"], marca = informacion["marca"], modelo = informacion["modelo"], talle = informacion["talle"], precio = informacion["precio"])
            
            indum.save()

            return render(request, "Appventas/inicio.html")

        else:
            miFormulario = indumentariaFormularios()

        return render(request, "Appventas/indumentariaformularios.html", {"miFormulario":miFormulario})

#def buscar(request):
    #if request.method == 'POST':

        #if request.POST['tipo'] == '1':

            #tipo = int(request.POST['tipo'])
