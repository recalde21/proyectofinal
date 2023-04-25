from django.urls import path
from .views import conversacion, conversaciones

urlpatterns = [
    #path('', nuevomensaje, name="nuevomensaje"),
    #path('mensaje', leermensaje, name="leermensaje"),
    #path('mensajes', vermensajes, name="vermensajes"),
    path("", conversaciones, name="mensajes"),
    path("conversacion", conversacion, name="conversacion")
]