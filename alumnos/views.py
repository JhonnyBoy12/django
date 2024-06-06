from django.shortcuts import render
from .models import Genero,Alumno

# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    #context = {"alumnos":Alumnos}
    #Alumnos = Alumno.objects.all()#select * from 
    context={}
    return render(request,"alumnos/index.html", context)

def index2(request):
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    context = {"alumnos":alumnos}
    return render(request, "alumnos/listadoSQL.html",context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(request, "alumnos/alumnos_list.html",context)

def alumnosAdd(request):
    if request.method != "POST":
        #NO ES UN POST, POR LO TANTO SE MUESTRA EL FORMULARIO PARA AGREGAR
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, "alumnos/alumno_add.html",context)
    else:
        print ("Entra por aqui")
    #es un post, por lo tanto se recuperan los datos del formulario
    #y se graban en la tabla
        
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo= "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj = Alumno.objects.create(

            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo =1
        )
        obj.save()
        context = {"mensaje": "Ok, datos guardados......"}
        return render(request,"alumnos/alumnos_add.html",context)



