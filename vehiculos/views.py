from django.shortcuts import render
from vehiculos.models import Vehiculo
# Create your views here.

def vehiculos(request):
   vehiculos=Vehiculo.objects.all()
   return render(request,"vehiculos/vehiculos.html",{"vehiculos":vehiculos})
