from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    link = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=1200, null=True, blank=True)
    imagen = models.ImageField(upload_to='images', null=True, blank=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return str(self.usuario)

    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url