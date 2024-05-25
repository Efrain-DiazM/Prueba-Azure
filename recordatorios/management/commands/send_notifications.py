from django.core.management.base import BaseCommand
from django.utils import timezone
from recordatorios.models import Recordatorio
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Command(BaseCommand):
    help = 'Envía notificaciones de recordatorios de medicamentos'

    def handle(self, *args, **options):
        now = timezone.now()
        recordatorios = Recordatorio.objects.filter(hora_alerta__lte=now)
        channel_layer = get_channel_layer()
        for recordatorio in recordatorios:
            async_to_sync(channel_layer.group_send)(
                "notificaciones",  
                {
                    "type": "enviar_notificacion",
                    "mensaje": f"Es hora de tomar tu medicamento: {recordatorio.nombre_medicamento}"
                }
            )
            self.stdout.write(self.style.SUCCESS(f"Notificación enviada para {recordatorio.nombre_medicamento}"))
