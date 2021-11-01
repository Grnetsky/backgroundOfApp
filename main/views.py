from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status

from main.userserializer import UserSerializer, CotentSerializer
from main.models import User, Content
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


class UserinfoViewset(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            instance = User.objects.get(username=username,password=password)
            serializer = self.get_serializer(instance)
            return Response({"code": 200, "data": serializer.data},status=status.HTTP_200_OK)
        except Exception:
            return Response({"code": 404, "errmsg": "用户名或密码错误"}, status=status.HTTP_404_NOT_FOUND)

class ContentViewset(GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    queryset = Content.objects.all()
    serializer_class = CotentSerializer


