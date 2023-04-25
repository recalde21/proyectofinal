from django.contrib import admin
from .models import Mensaje

# Register your models here.

class MensajeAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'usuario_rem',
		'usuario_dest',
		'mensaje',
		'fecha',
        'leido',
	)
admin.site.register(Mensaje, MensajeAdmin)