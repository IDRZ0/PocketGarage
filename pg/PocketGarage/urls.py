
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('PocketGarage/index1.html/',views.home),
	path('PocketGarage/index2.html/',views.autos),
	path('PocketGarage/index3.html/',views.repuestos),
	path('PocketGarage/index10.html/',views.home1),
	path('PocketGarage/index20.html/',views.autos1),
	path('PocketGarage/index30.html/',views.repuestos1),
	path('PocketGarage/register.html/',views.register),
	path('PocketGarage/login.html/',views.login),
	path('PocketGarage/repuesto.html/',views.publirepuesto),
	path('PocketGarage/vehiculo.html/',views.publiauto),
	path('PocketGarage/publicaciones.html/',views.mispublis),
]
