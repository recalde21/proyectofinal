from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    subtitulo = models.CharField(max_length=200, null=True)
    cuerpo = models.CharField(max_length=1200, null=True)
    autor = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='images', null=True, blank=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo

    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url