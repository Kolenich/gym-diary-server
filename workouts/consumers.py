import json

from channels.generic.websocket import WebsocketConsumer


class WorkoutConsumer(WebsocketConsumer):
    def receive(self, text_data):
        print(self.scope['user'])
        text_data_json = json.loads(text_data)

        self.send(text_data=json.dumps(text_data_json))