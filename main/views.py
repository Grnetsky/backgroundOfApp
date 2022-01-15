import time

from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import base64
from main.userserializer import UserSerializer, CotentSerializer
from main.models import User, Content
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from utils.csrf import CsrfExemptSessionAuthentication
from .serializer import MyTokenObtainPairSerializer

MY_IP = 'http://127.0.0.1:8000/'
from rest_framework_simplejwt.views import TokenViewBase, TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from .serializer import *
from .models import *


class MyTokenObtainPairView(TokenObtainPairView):
    """
    自定义得到token username: 账号或者密码 password: 密码或者验证码
    """
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenViewBase):
    """
    自定义刷新token refresh: 刷新token的元素
    """
    serializer_class = TokenRefreshSerializer
class UserinfoViewset(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication ]
    permission_classes = [IsAuthenticated, ]

    def retrieve(self, request, *args, **kwargs):
        print(request.user)
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        try:
            instance = authenticate(username=username, password=password)
            if instance is not None:
                print(request.user)
                serializer = self.get_serializer(instance)
                return Response({"code": 200, "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"code": 404, "errmsg": "用户名或密码错误"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            # return JsonResponse({"code": 404, "errmsg": "用户名或密码错误"})
            return Response({"code": 404, "errmsg": "用户名或密码错误"}, status=status.HTTP_404_NOT_FOUND)

    def userlogout(self, request):
        # user = authenticate(username=request.)
        print(request.user)
        logout(request)
        # if usr:
        #     print("用户已登录")
        #     logout(request)
        #     return Response({'mes': '退出成功'})
        return Response({'code': 400, 'msg': '出问题了'})

'''文本视图'''

class ContentView(GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Content.objects.all()
    serializer_class = CotentSerializer

    # 获取笔记
    def get(self, request, pk):
        contens = Content.objects.filter(author_id=pk)
        serilizer = CotentSerializer(contens, many=True)
        return Response({'code': 200, 'data': serilizer.data}, status=status.HTTP_200_OK)

    def post(self,request):
        user = request.user

        return

'''退出登录'''

class Logoutview(APIView):
    def post(self, request):
        print(request.user, '退出')
        logout(request)
        return Response({'code': 200, 'msg': '退出登录成功！'})


class RegisterCheck(APIView):
    authentication_classes = []
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            return Response({'code': 400, 'data': '用户已存在'})
        else:
            return Response({'code': 200, 'data': '用户名可用'})


class Registe(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = User.objects.create_user(username=request.data.get("username"), password=request.data.get("password"),
                                        sex=1)
        user.save()
        info = UserSerializer(user)
        return Response({'code': 200, 'data': info.data})


class ChangeHeadPortrait(APIView):
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        head_file = request.data.get('file')
        user = User.objects.get(username=request.user.username)
        if user.head_portrait != '/head_portrait/head_portrait.jpg':
            user.head_portrait.delete()
        user.head_portrait = head_file
        print(user.head_portrait)
        user.save()
        return Response({'code': 200, 'msg': '头像更改成功', 'data': MY_IP + 'media/' + str(user.head_portrait)})

def test(request):
    print(request.POST.get("id"))
    # mgr = socketio.KombuManager("amqp://admin:admin@localhost:5672//")  # amqp://用户名:密码@localhost：5672/v_host名
    # mgr.emit(event="message",data={"msg":"这是django发送的im通讯"})
    # sio.enter_room(sid=str(request.POST.get("id")),room='we')
    # sio.enter_room(sid=request.POST.get("id"),room="we",namespace=None)
    return JsonResponse({"msg":"ok"})