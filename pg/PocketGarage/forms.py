from django import forms
from PocketGarage.models import *

class RegisterForm(forms.Form):
	CI = forms.IntegerField()
	Nombre_Completo = forms.CharField(max_length=50)
	Telefono = forms.IntegerField()
	Email = forms.EmailField(required=False)
	Contraseña = forms.CharField(max_length=25,widget=forms.PasswordInput)
	Verificar_Contraseña = forms.CharField(max_length=25,widget=forms.PasswordInput)
	class Meta:
		model = Usuario
		fields = ('CI','Nombre_Completo','Telefono','Email','Contraseña')
	def clean_CI(self):
		CI = self.cleaned_data['CI']
		if Usuario.objects.filter(CI=CI).exists():
			raise forms.ValidationError("Ya existe un usuario con ese CI")
		return CI

class LoginForm(forms.Form):
	CI = forms.IntegerField()
	Contraseña = forms.CharField(max_length=25,widget=forms.PasswordInput)

class RepuestoForm(forms.Form):
	Descripcion = forms.CharField(max_length=200)
	Foto = forms.ImageField()
	Precio = forms.CharField(max_length=25)
	Informacion_Vendedor = forms.CharField(max_length=150)
	class Meta:
		model = Repuesto
		fields = ('Descripcion','Foto','Precio','Informacion_Vendedor')

class AutoForm(forms.Form):
	Modelo = forms.CharField(max_length=50)
	Precio = forms.CharField(max_length=25)
	Foto = forms.ImageField()
	Ficha_Tecnica = forms.CharField(max_length=500)
	Informacion_Propietario = forms.CharField(max_length=150)
	class Meta:
		model = Vehiculo
		fields = ('Modelo','Precio','Foto','Ficha_Tecnica','Informacion_Propietario')