# recordatorios/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificacionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notificaciones", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notificaciones", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mensaje = text_data_json['mensaje']

        await self.channel_layer.group_send(
            "notificaciones",
            {
                'type': 'enviar_notificacion',
                'mensaje': mensaje
            }
        )

    async def enviar_notificacion(self, event):
        mensaje = event['mensaje']
        await self.send(text_data=json.dumps({
            'mensaje': mensaje
        }))
