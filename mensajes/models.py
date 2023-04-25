from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensaje(models.Model):
    usuario_rem = models.ForeignKey(User, related_name='usuario_rem', null=True, blank=True, on_delete=models.CASCADE)
    usuario_dest = models.ForeignKey(User, related_name='usuario_dest', null=True, blank=True, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    def __str__(self):
        return self.mensaje