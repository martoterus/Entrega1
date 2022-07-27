
# Create your views here.
from doctest import ELLIPSIS_MARKER
from django.shortcuts import render
from django.http import HttpResponse
from Appventas.models import bicicletas, repuestos, indumentaria
from Appventas.forms import bicisformulario, repuestosFormulario, indumentariaFormularios

# Create your views here.


def inicio(request):

    return render(request, "inicio.html")

def Formulariobicis(request):

    if request.method == 'POST':
        BiciFormulario=bicisformulario(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",BiciFormulario ) 

        if BiciFormulario.is_valid():
            print("Entro al 2° if")
            data=BiciFormulario.cleaned_data

            BICI=bicicletas(marca=data['Marca'],modelo=data['Modelo'],rodado=data['Rodado'],color=data['Color'],fecha_fabricacion=data['Fecha_Fabricacion'],precio=data['Precio'],)
            BICI.save()
            return render(request, "inicio.html")
        else:
            return render (request,"inicio2.html")
    else:
        BiciFormulario=bicisformulario()
        return render(request,"biciFormulario.html", {"BiciFormulario": BiciFormulario})
# def Formulariobici(request):
#     print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
#     print("method:",request.POST )
#     if request.method == "POST":

#         formulario=bicicletas(request.POST['Marca'],request.POST['Modelo'],request.POST['Rodado'],request.POST['Color'],request.POST['Fecha_Fabricacion'],request.POST['Precio'],)
#         formulario.save()
#         return render(request,"inicio.html")
#     return render (request,"biciFormulario.html")

# def Formulariobicis(request):

#     if request.method == 'POST':

#         miFormulario = bicisformulario(request.POST)

#         print(miFormulario)

#         if miFormulario.is_valid():

#             informacion = miFormulario.cleaned_data

#             bici = bicicletas(marca = informacion["marca"], modelo = informacion["modelo"], rodado = informacion["rodado"], color = informacion["color"], fecha_fabricacion = informacion["fecha_fabricacion"], precio = informacion["precio"])
            
#             bici.save()

#             return render(request, "Appventas/inicio.html")

#     else:
#         miFormulario = bicisformulario()

#         return render(request, "Appventas/biciformulario.html", {"miFormulario":miFormulario})
        

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
