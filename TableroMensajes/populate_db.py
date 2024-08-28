import os
import django

# Configurar Django para usar los settings del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TableroMensajes.settings')
django.setup()

from mensajes.models import Mensaje
from django.utils import timezone

# Datos de los mensajes
mensajes = [
    {'texto': 'Hola, ¿cómo estás?', 'remitente': 'Juan', 'destinatario': 'María', 'fecha_envio': timezone.now()},
    {'texto': 'Reunión a las 10 am', 'remitente': 'Pedro', 'destinatario': 'María', 'fecha_envio': timezone.now()},
    {'texto': 'No olvides enviar el informe', 'remitente': 'Luis', 'destinatario': 'María', 'fecha_envio': timezone.now()},
]

# Poblar la base de datos
for msg in mensajes:
    Mensaje.objects.create(**msg)

print("Datos de prueba añadidos con éxito.")
