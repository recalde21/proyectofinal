from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Perfil

class UserChangeForm(forms.ModelForm):
	username = forms.CharField(
		label='Nombre de usuario*',
		widget=forms.TextInput(attrs={"class":"form-control"})
	)
	email = forms.EmailField(
		label=("Correo electrónico*"),
		widget=forms.TextInput(attrs={"class":"form-control"})
	)
	password = forms.CharField(
		label='Nueva contraseña*',
		required = False,
		widget=forms.PasswordInput(attrs={"class":"form-control"})
	)
	class Meta:
		model = User
		fields = '__all__'

	def save(self, commit=True):
		user = super(UserChangeForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class ProfileChangeForm(forms.ModelForm):
	link = forms.CharField(
		label='Enlace a web',
		required=False,
		widget=forms.TextInput(attrs={"class":"form-control"})
	)
	descripcion = forms.CharField(
		label=("Descripción"),
		required=False,
		widget=forms.TextInput(attrs={"class":"form-control"})
	)
	imagen = forms.ImageField(
        label='Imagen*',
        required=False,
        widget=forms.FileInput(attrs={
            "class":"form-control",
        })
    )

	class Meta:
		model = Perfil
		#fields = '__all__'
		fields = (
			'link',
			'descripcion',
			'imagen'
		)

