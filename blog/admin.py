from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'autor',
		'titulo',
		'subtitulo',
		'cuerpo',
        'fecha',
        'imagen',
        'deleted',
	)
admin.site.register(Blog, BlogAdmin)