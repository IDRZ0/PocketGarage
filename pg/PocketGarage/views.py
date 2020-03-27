from django.shortcuts import render, redirect
from PocketGarage.forms import *
from PocketGarage.models import *
from django.core.exceptions import ObjectDoesNotExist

def home(request):
	return render(request,'PocketGarage/index1.html')

def autos(request):
	lista_autos= Vehiculo.objects.all()
	return render(request,'PocketGarage/index2.html',{"Vehiculos":lista_autos})

def repuestos(request):
	lista_repuestos = Repuesto.objects.all()
	return render(request,'PocketGarage/index3.html',{"Repuestos":lista_repuestos})

def home1(request):
	return render(request,'PocketGarage/index10.html')

def autos1(request):
	lista_autos= Vehiculo.objects.all()
	return render(request,'PocketGarage/index20.html',{"Vehiculos":lista_autos})

def repuestos1(request):
	lista_repuestos = Repuesto.objects.all()
	return render(request,'PocketGarage/index30.html',{"Repuestos":lista_repuestos})

def register(request):
	if request.method=="POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			CI = form.cleaned_data['CI']
			Nombre = form.cleaned_data['Nombre_Completo']
			Telefono = form.cleaned_data['Telefono']
			Email = form.cleaned_data['Email']
			Contraseña = form.cleaned_data['Contraseña']
			Contraseña1 = form.cleaned_data['Verificar_Contraseña']
			if Contraseña==Contraseña1:
				user=Usuario(CI=CI,Nombre=Nombre,Telefono=Telefono,Email=Email,Contraseña=Contraseña)
				user.save()
				return redirect('/PocketGarage/login.html/')
	else:
		form = RegisterForm()
	return render(request,'PocketGarage/register.html',{'form':form})

def login(request):
	if request.method=="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			CI = form.cleaned_data['CI']
			Contraseña = form.cleaned_data['Contraseña']
			try:
				user = Usuario.objects.get(CI=CI)
				if Contraseña==user.Contraseña:
					return redirect('/PocketGarage/index10.html/')
			except ObjectDoesNotExist:
				form = LoginForm()
				return render(request,'PocketGarage/login.html',{'form':form})
	else:
		form = LoginForm()
	return render(request,'PocketGarage/login.html',{'form':form})

def publirepuesto(request):
	if request.method=="POST":
		form = RepuestoForm(request.POST, request.FILES)
		if form.is_valid():
			Descripcion = form.cleaned_data['Descripcion']
			Foto = form.cleaned_data['Foto']
			Precio = form.cleaned_data['Precio']
			Informacion_Vendedor = form.cleaned_data['Informacion_Vendedor']
			repuesto = Repuesto(Descripcion=Descripcion,Foto=Foto,Precio=Precio,Info_Vendedor=Informacion_Vendedor)
			repuesto.save()
			return redirect('/PocketGarage/index30.html/')
	else:
		form = RepuestoForm()
	return render(request,'PocketGarage/repuesto.html',{'form':form})

def publiauto(request):
	if request.method=="POST":
		form = AutoForm(request.POST, request.FILES)
		if form.is_valid():
			Modelo = form.cleaned_data['Modelo']
			Precio = form.cleaned_data['Precio']
			Foto = form.cleaned_data['Foto']
			Ficha_Tecnica = form.cleaned_data['Ficha_Tecnica']
			Informacion_Propietario = form.cleaned_data['Informacion_Propietario']
			vehiculo = Vehiculo(Modelo=Modelo,Precio=Precio,Foto=Foto,FichaTecnica=Ficha_Tecnica,Info_Propietario=Informacion_Propietario)
			vehiculo.save()
			return redirect('/PocketGarage/index20.html/')
	else:
		form = AutoForm()
	return render(request,'PocketGarage/vehiculo.html',{'form':form})