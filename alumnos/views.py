from django.shortcuts import render
from .models import Genero,Alumno

# Create your views here.
def index(request):
    Alumnos = Alumno.objects.all()#select * from 
    context = {"alumnos":Alumnos}
    return render(request,"alumnos/index.html", context)

def index2(request):
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    context = {"alumnos":alumnos}
    return render(request, "alumnos/listadoSQL.html",context)