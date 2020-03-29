from django.db import models
from django.contrib.auth.models import User
from django import forms

class Usuario(models.Model):
    CI = models.IntegerField(unique=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.IntegerField()
    Email = models.EmailField(blank=True)
    Contraseña = models.CharField(max_length=25)
    def __str__(self):
        return self.Nombre

class Repuesto(models.Model):
    Descripcion = models.CharField(max_length=200)
    Foto = models.ImageField(upload_to='PocketGarage/repuestos/')
    Precio = models.CharField(max_length=25)
    CI = models.IntegerField(default=0)
    Nombre_Vendedor = models.CharField(max_length=150)
    Telefono_Vendedor = models.IntegerField()
    Email_Vendedor = models.EmailField(blank=True)
    def __str__(self):
        return self.Descripcion

class Vehiculo(models.Model):
    Marca = models.CharField(max_length=25)
    Modelo = models.CharField(max_length=25)
    Año = models.IntegerField()
    Color = models.CharField(max_length=30)
    Motor = models.CharField(max_length=20)
    Precio = models.CharField(max_length=25)
    Foto = models.ImageField(upload_to='PocketGarage/vehiculos/')
    Especificaciones = models.CharField(max_length=500)
    CI = models.IntegerField(default=0)
    Nombre_Propietario = models.CharField(max_length=150)
    Telefono_Propietario = models.IntegerField()
    Email_Propietario = models.EmailField(blank=True)
    def __str__(self):
        return self.Marca + self.Modelo
