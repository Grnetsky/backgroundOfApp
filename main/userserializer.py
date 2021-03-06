from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from main.models import User, Content


class CotentSerializer(ModelSerializer):
    '''用户笔记序列化器'''

    class Meta:
        model = Content
        fields = '__all__'


from main.models import Content


class UserSerializer(ModelSerializer):
    '''用户信息序列化器'''
    contents = CotentSerializer(many=True,read_only=True)
    # contents = serializers.SlugRelatedField(slug_field='title',read_only=True,many=True)

    # contents = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='content-detail')
    class Meta:
        model = User
        exclude =['password']
