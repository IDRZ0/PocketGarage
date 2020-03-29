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
	class Meta:
		model = Repuesto
		fields = ('Descripcion','Foto','Precio','CI','Nombre_Vendedor','Telefono_Vendedor','Email_Vendedor')

class AutoForm(forms.Form):
	Marca = forms.CharField(max_length=25)
	Modelo = forms.CharField(max_length=25)
	Año = forms.IntegerField()
	Color = forms.CharField(max_length=30)
	Motor = forms.CharField(max_length=20)
	Precio = forms.CharField(max_length=25)
	Foto = forms.ImageField()
	Especificaciones = forms.CharField(max_length=500)
	class Meta:
		model = Vehiculo
		fields = ('Marca','Modelo','Año','Color','Motor','Precio','Foto','Especificaciones','CI','Nombre_Propietario','Telefono_Propietario','Email_Propietario')