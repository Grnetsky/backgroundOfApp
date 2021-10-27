from rest_framework.serializers import ModelSerializer

from main.models import User, Content


class UserSerializer(ModelSerializer):
    '''用户信息序列化器'''

    class Meta:
        model = User
        exclude = ["password"]


class CotentSerializer(ModelSerializer):
    '''用户笔记序列化器'''

    class Meta:
        model = Content
        fields = '__all__'
        depth = 1
