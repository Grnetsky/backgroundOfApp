import json

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from main.models import User
class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        group = self.scope['url_route']['kwargs'].get("group")
        self.accept()  # 允许创建连接
        # self.close()

        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)# 加群

    def websocket_disconnect(self, message):
        group = self.scope['url_route']['kwargs'].get("group")
        async_to_sync(self.channel_layer.group_discard)(group, self.channel_name)
        raise StopConsumer()

    def websocket_receive(self, message):
        self.send("服务器已接受信息")
        obj = json.loads(message["text"])
        print(obj["data"])
        group = self.scope['url_route']['kwargs'].get("group")
        async_to_sync(self.channel_layer.group_send)(group,{"type":'send.group.message', "message":message})

    def send_group_message(self,event):
        text = event["message"]["text"]
        self.send(text)