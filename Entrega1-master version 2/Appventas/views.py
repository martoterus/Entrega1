
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

def bicis(request):

    if request.method == 'POST':

        miFormulario = bicisformulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            bici = bicicletas(marca = informacion['Marca'], modelo = informacion['Modelo'], rodado = informacion['Rodado'], color = informacion['Color'], precio = informacion['Precio'])
            
            bici.save()

            return render(request, "volver.html")

        else:
            miFormulario = bicisformulario()

        return render(request, "biciformulario.html", {"miFormulario":miFormulario})

    if request.method == 'GET':
   
        miFormulario = bicisformulario()

        return render(request, "biciformulario.html", {"miFormulario":miFormulario})


        

def repuesto(request):

    if request.method == 'POST':

        miFormulario1 = repuestosFormulario(request.POST)

        print(miFormulario1)

        if miFormulario1.is_valid:

            informacion1 = miFormulario1.cleaned_data

            rep = repuestos(tipo = informacion1["Tipo"], marca = informacion1["Marca"], modelo = informacion1["Modelo"], fabricante = informacion1["Fabricante"], precio = informacion1["Precio"])
            
            rep.save()

            return render(request, "volver.html")

        else:
            miFormulario1 = repuestosFormulario()

        return render(request, "repuestosformulario.html", {"miFormulario1":miFormulario1})

    if request.method == 'GET':
   
        miFormulario1 = repuestosFormulario()

        return render(request, "repuestosformulario.html", {"miFormulario1":miFormulario1})


def indumentarias(request):

    if request.method == 'POST':

        miFormulario2 = indumentariaFormularios(request.POST)

        print(miFormulario2)

        if miFormulario2.is_valid:

            informacion2 = miFormulario2.cleaned_data

            indum = indumentaria(tipo = informacion2["Tipo"], marca = informacion2["Marca"], modelo = informacion2["Modelo"], talle = informacion2["Talle"], precio = informacion2["Precio"])
            
            indum.save()

            return render(request, "volver.html")

        else:
            miFormulario2 = indumentariaFormularios()

        return render(request, "indumentariaformularios.html", {"miFormulario2":miFormulario2})

    if request.method == 'GET':
   
        miFormulario2 = indumentariaFormularios()

        return render(request, "indumentariaformulario.html", {"miFormulario2":miFormulario2})


def busquedabicis(request):

    return render(request, "busquedabicis.html")
    

def buscar(request):

    if request.GET['Marca']:

	     #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
         marca = request.GET['Marca']

         listabici = bicicletas.objects.filter(marca__icontains=marca)
        
         return render(request, "resultadobusqueda.html", {"Modelo": listabici, "Marca": marca})

    else: 
         respuesta = "No enviaste datos"

         #No olvidar from django.http import HttpResponse
         return HttpResponse(respuesta)
