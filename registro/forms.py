from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
	username = forms.CharField(
		label='Nombre de usuario*',
		widget=forms.TextInput(attrs={"class":"form-control"})
	)
	email = forms.EmailField(
		label=("Correo electrónico*"),
		widget=forms.TextInput(attrs={"class":"form-control"})
	)
	password1 = forms.CharField(
		label='Contraseña*',
		widget=forms.PasswordInput(attrs={"class":"form-control"})
	)
	password2 = forms.CharField(
		label=("Constraseña (confirmación)*"),
		widget=forms.PasswordInput(attrs={"class":"form-control"})
	)

	class Meta:
		model = User
		fields  = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email =self.cleaned_data["email"]
		if commit:
			user.save()
		return user

