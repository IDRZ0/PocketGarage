from django.shortcuts import render, redirect
from PocketGarage.forms import *
from PocketGarage.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

def home(request):
	return render(request,'PocketGarage/index1.html')

def autos(request):
	lista_autos= Vehiculo.objects.all()
	return render(request,'PocketGarage/index2.html',{"Vehiculos":lista_autos})

def repuestos(request):
	lista_repuestos = Repuesto.objects.all()
	return render(request,'PocketGarage/index3.html',{"Repuestos":lista_repuestos})

def home1(request):
	CI = request.session.get('user_CI')
	user = Usuario.objects.get(CI=CI)
	name = user.Nombre
	return render(request,'PocketGarage/index10.html',{'name':name})

def autos1(request):
	lista_autos= Vehiculo.objects.all()
	return render(request,'PocketGarage/index20.html',{"Vehiculos":lista_autos})

def repuestos1(request):
	lista_repuestos = Repuesto.objects.all()
	return render(request,'PocketGarage/index30.html',{"Repuestos":lista_repuestos})

def mispublis(request):
	CI = request.session.get('user_CI')
	lista_autos= Vehiculo.objects.filter(CI=CI)
	lista_repuestos = Repuesto.objects.filter(CI=CI)
	return render(request,'PocketGarage/publicaciones.html',{'Vehiculos':lista_autos,'Repuestos':lista_repuestos})

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
				messages.error(request,'Las contraseñas no coinciden!')
		else:
			messages.error(request,'Ya existe un usuario con ese CI!')
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
				request.session['user_CI'] = CI
				if Contraseña==user.Contraseña:
					return redirect('/PocketGarage/index10.html/')
			except ObjectDoesNotExist:
				form = LoginForm()
				return render(request,'PocketGarage/login.html',{'form':form})
	else:
		form = LoginForm()
	return render(request,'PocketGarage/login.html',{'form':form})

def publirepuesto(request):
	CI = request.session.get('user_CI')
	user = Usuario.objects.get(CI=CI)
	if request.method=="POST":
		form = RepuestoForm(request.POST, request.FILES)
		if form.is_valid():
			Descripcion = form.cleaned_data['Descripcion']
			Foto = form.cleaned_data['Foto']
			Precio = form.cleaned_data['Precio']
			repuesto = Repuesto(Descripcion=Descripcion,Foto=Foto,Precio=Precio,CI=user.CI,Nombre_Vendedor=user.Nombre,Telefono_Vendedor=user.Telefono,Email_Vendedor=user.Email)
			repuesto.save()
			return redirect('/PocketGarage/index30.html/')
	else:
		form = RepuestoForm()
	return render(request,'PocketGarage/repuesto.html',{'form':form})

def publiauto(request):
	CI = request.session.get('user_CI')
	user = Usuario.objects.get(CI=CI)
	if request.method=="POST":
		form = AutoForm(request.POST, request.FILES)
		if form.is_valid():
			Marca = form.cleaned_data['Marca']
			Modelo = form.cleaned_data['Modelo']
			Año = form.cleaned_data['Año']
			Color = form.cleaned_data['Color']
			Motor = form.cleaned_data['Motor']
			Precio = form.cleaned_data['Precio']
			Foto = form.cleaned_data['Foto']
			Especificaciones = form.cleaned_data['Especificaciones']
			vehiculo = Vehiculo(Marca=Marca,Modelo=Modelo,Año=Año,Color=Color,Motor=Motor,Precio=Precio,Foto=Foto,Especificaciones=Especificaciones,CI=user.CI,Nombre_Propietario=user.Nombre,Telefono_Propietario=user.Telefono,Email_Propietario=user.Email)
			vehiculo.save()
			return redirect('/PocketGarage/index20.html/')
	else:
		form = AutoForm()
	return render(request,'PocketGarage/vehiculo.html',{'form':form})

def error404(request,exception):
	return render(request,'PocketGarage/error404.html',status=404)

def error500(request):
	return render(request,'PocketGarage/error500.html',status=500)