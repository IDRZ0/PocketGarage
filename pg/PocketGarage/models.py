from django.db import models
from django.contrib.auth.models import User
from django import forms

class Usuario(models.Model):
    CI = models.IntegerField(unique=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Email = models.EmailField(blank=True)
    Contraseña = models.CharField(max_length=25, default='')
    def __str__(self):
        return self.Nombre

class Repuesto(models.Model):
    Descripcion = models.CharField(max_length=200)
    Foto = models.ImageField(upload_to='PocketGarage/repuestos/')
    Precio = models.CharField(max_length=25)
    Info_Vendedor = models.CharField(max_length=150,default='')
    def __str__(self):
        return self.Descripcion

class Vehiculo(models.Model):
    Modelo = models.CharField(max_length=50)
    Precio = models.CharField(max_length=25)
    Foto = models.ImageField(upload_to='PocketGarage/vehiculos/')
    FichaTecnica = models.CharField(max_length=500)
    Info_Propietario = models.CharField(max_length=150,default='')
    def __str__(self):
        return self.Modelo
