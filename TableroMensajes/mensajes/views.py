from django.shortcuts import render

# Create your views here.

from .models import Mensaje

def mensajes_recibidos(request):
    destinatario = request.GET.get('destinatario', 'María')  # Filtrar por destinatario
    mensajes = Mensaje.objects.filter(destinatario=destinatario)
    return render(request, 'mensajes/recibidos.html', {'mensajes': mensajes})
