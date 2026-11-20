from django.shortcuts import render, redirect
from .models import Persona
from .forms import FormPersona
from django.http import Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def IniciarSesion(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        pwrd = request.POST['passwrd']
        
        usuario = authenticate(request, username=nombre, password=pwrd)
        
        if usuario is not None:
            login(request, usuario)
            return redirect("ListaPersona")
        else:
            return render(request, "IniciarSesion.html", {"mensaje": 'Credenciales invalidas'})
        
    elif request.method == 'GET':
        return render(request,"IniciarSesion.html")
    else:
        return Http404()

def RegistrarUsuario(request):
    if request.method == 'POST':
        pwrd1 = request.POST['passwrd']
        pwdr2 = request.POST['passwrd2']
        
        if pwrd1 == pwdr2:
            nombre = request.POST['nombre']
            User.objects.create_user(username=nombre, password=pwrd1)
            return render(request, "IniciarSesion.html", {"mensaje": 'Usuario creado'})
        else:
            return render(request, "RegistrarUsuario.html", {'mensaje':'Contraseñas no coinciden'})
    else:
        return render(request, "RegistrarUsuario.html")
    
def Logout(request):
    logout(request)
    return render(request, "IniciarSesion.html")
             

def ViewListar(request):
    persons = Persona.objects.all()
    return render(request,"Listar.html", {'personas':persons})

@login_required
def ViewFormulario(request):
    if request.method == "GET":
        form = FormPersona()
        return render(request,"FormularioPersona.html",{'form':form})
    
    elif request.method == "POST":
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        direccion = request.POST['direccion']
        correo_electronico = request.POST['correo_electronico']
        fecha_nacimiento = request.POST['fecha_nacimiento']

        person = Persona(rut = rut, nombre = nombre, apellidos = apellidos,
                         direccion= direccion, correo_electronico = correo_electronico,
                         fecha_nacimiento = fecha_nacimiento)

        person.save()

        return redirect("ListaPersona")
    else:
        return Http404()

@login_required
def ViewEliminar(request):
    if request.method == 'GET':
        rut = request.GET['rut']
        person = Persona.objects.get(rut=rut)
        return render(request, "Eliminar.html",{'persona':person})
    else:
        return Http404()

@login_required
def ConfirmarEliminar(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        person = Persona.objects.get(rut=rut)
        person.delete()
        return redirect("ListaPersona")

    else:
        return Http404()

@login_required    
def ViewActualizar(request):
    if request.method == 'GET':
        rut = request.POST['rut']
        person = Persona.objects.get(rut=rut)
        return render(request, "Actualizar.html",{"persona":person})
    
    elif request.method == 'POST':
        rut = request.POST['rut']
        person = Persona.objects.get(rut=rut)
        person.nombre = request.POST['nombre']
        person.apellidos = request.POST['apellidos']
        person.correo_electronico = request.POS['correo_electronico']
        person.direccion = request.POST['direccion']
        person.fecha_nacimiento = request.POST['fecha_nacimiento']
        
        person.save(force_update=True)
        
        return redirect("ListaPersona")
    else:
        return Http404()