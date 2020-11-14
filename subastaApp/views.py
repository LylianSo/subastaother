from django.shortcuts import render, HttpResponse

"""
from rest_framework import viewsets
from .models import Vehiculo

from .serializer import VehiculoSerializer

# Create your views here.

class VehiculoViewSet(viewsets.ModelViewSet):
    serializer_class = VehiculoSerializer
    queryset = Vehiculo.objects.all()"""

def home(request):

    return render(request,"subastaApp/home.html")



def detalle(request):

    return render(request,"subastaApp/detalle.html")

def login(request):

    return render(request,"subastaApp/login.html")

def contacto(request):

    return render(request,"subastaApp/contacto.html")

def servicios(request):

    return render(request,"subastaApp/servicios.html")


