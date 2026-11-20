"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import ViewFormulario, ViewListar, ViewEliminar, ConfirmarEliminar, ViewActualizar
from .views import IniciarSesion, RegistrarUsuario, Logout
urlpatterns = [
    path('',RegistrarUsuario, name="RegistrarUsuario"),
    path('iniciar_sesion/', IniciarSesion, name="IniciarSesion"),
    path('logout/', Logout, name="Logout"),
    path('ingreso/', ViewFormulario, name="FormularioPersona"),
    path('listar/', ViewListar, name="ListaPersona"),
    path('eliminar', ViewEliminar, name="EliminarPersona"),
    path('confirmar/', ConfirmarEliminar, name="ConfirmaEliminar" ),
    path('actualizar', ViewActualizar, name="ActualizarPersona" )
]
