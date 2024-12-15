# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class InventoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'inventory_updates'
        # הצטרפות לקבוצה של עדכונים בזמן אמת
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # יציאה מהקבוצה
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # קבלה ושליחה של נתונים (במקרה הזה לא נחוץ)
        pass

    async def send_inventory_update(self, event):
        # שליחה של עדכון למלאי לכל החברים בקבוצה
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
