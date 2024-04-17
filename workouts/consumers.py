from channels.generic.websocket import AsyncWebsocketConsumer


class WorkoutConsumer(AsyncWebsocketConsumer):
    group = 'workouts'

    async def connect(self):
        # Join group
        await self.channel_layer.group_add(self.group, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(self.group, self.channel_name)
