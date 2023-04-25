from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AuthenticationForm(AuthenticationForm):
	username = forms.CharField(
		label='Nombre de usuario*',
		widget=forms.TextInput(attrs={"class":"form-control"})
	)
	password = forms.CharField(
		label='Contraseña*',
		widget=forms.PasswordInput(attrs={"class":"form-control"})
	)

	class Meta:
		model = User
		fields  = ("username", "password")

	def __init__(self, *args, **kwargs):
		super(AuthenticationForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.error_messages = {'required':'{fieldname} is required'.format(
            fieldname=field.label)}