import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from chatapp.models import Room, Message
from users.models import CustomUser as User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_slug']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message")
        username = text_data_json.get("username")
        room_name = text_data_json.get("room_name")
        image = text_data_json.get("image")
        location = text_data_json.get("location")

        if message or image or location:
            await self.save_message(message, username, room_name, image, location)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "username": username,
                    "room_name": room_name,
                    "image": image,
                    "location": location,
                }
            )

    async def chat_message(self, event):
        message = event.get("message")
        username = event.get("username")
        image = event.get("image")
        location = event.get("location")

        await self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "image": image,
            "location": location,
        }))

    @sync_to_async
    def save_message(self, message, username, room_name, image, location):
        user = User.objects.get(username=username)
        room = Room.objects.get(name=room_name)

        Message.objects.create(user=user, room=room, content=message, image=image, location=location)
