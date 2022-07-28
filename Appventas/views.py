
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
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            bici=bicicletas(marca=data['Marca'],modelo=data['Modelo'],rodado=data['Rodado'],color=data['Color'],precio=data['Precio'],)
            bici.save()
            return render(request, "inicio.html")
       # else:
        #    return render (request,"inicio2.html")
    else:
        BiciFormulario=bicisformulario()
        return render(request,"biciFormulario.html", {"BiciFormulario": BiciFormulario})


def Formulariorepuestos(request):

    if request.method == 'POST':
                        #forms.py
        RepuFormulario=repuestosFormulario(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",RepuFormulario ) 

        if RepuFormulario.is_valid():
            print("Entro al 2° if")
            data=RepuFormulario.cleaned_data
            #En la tabla que creo con la clase (models) le cargo los datos del formulario de Django(forms)
                     #models.py   (como se lee esto?: tipo=data['Tipo'])          
            repuesto=repuestos(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],fabricante=data['Fabricante'],precio=data['Precio'],)
            repuesto.save()
            return render(request, "inicio.html")
        else:
            return render (request,"inicio2.html")
    else:
        RepuFormulario=repuestosFormulario()
        return render(request,"repuestoFormulario.html", {"RepuestosFormularios":RepuFormulario})        

def Formularioindumentarias(request):

    if request.method == 'POST':
        InduFormulario=indumentariaFormularios(request.POST)
        print("method:", request.method) #Va  a imprimir por terminal el método que utilizamos. 
        print("Formulario:",InduFormulario ) 

        if InduFormulario.is_valid():
            print("Entro al 2° if")
            data=InduFormulario.cleaned_data
            #En la tabla que creo con la clase le cargo los datos del formulario de Django
            Indu=indumentaria(tipo=data['Tipo'],marca=data['Marca'],modelo=data['Modelo'],talle=data['Talle'],precio=data['Precio'],)
            Indu.save()
            return render(request, "inicio.html")
        else:
            return render (request,"inicio2.html")
    else:
        InduFormulario=indumentariaFormularios()
        return render(request,"indumentariaFormulario.html", {"IndumentariaFormularios": InduFormulario})