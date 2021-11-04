from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from main.userserializer import UserSerializer, CotentSerializer
from main.models import User, Content
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.views import APIView

from utils.csrf import CsrfExemptSessionAuthentication


class UserinfoViewset(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JSONWebTokenAuthentication, ]

    def retrieve(self, request, *args, **kwargs):

        username = request.data.get("username")
        password = request.data.get("password")
        try:
            instance = authenticate(username=username, password=password)
            if instance is not None:
                login(request, instance)
                print(request.user)
                serializer = self.get_serializer(instance)
                return Response({"code": 200, "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"code": 404, "errmsg": "用户名或密码错误"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            # return JsonResponse({"code": 404, "errmsg": "用户名或密码错误"})
            return Response({"code": 404, "errmsg": "用户名或密码错误"}, status=status.HTTP_404_NOT_FOUND)

    def createuser(self, request):
        user = User.objects.create_user(username=request.data.get("username"), password=request.data.get("password"),
                                        sex=1)
        user.save()
        info = UserSerializer(user)
        return Response({'code': 200, 'data': info.data})

    def userlogout(self, request):
        # user = authenticate(username=request.)
        print(request.user)
        logout(request)
        # if usr:
        #     print("用户已登录")
        #     logout(request)
        #     return Response({'mes': '退出成功'})
        return Response({'code': 400, 'msg': '出问题了'})

    def test(self, request):
        print(request.user)
        return Response({'code': 'ok'})

'''文本视图'''
class ContentViewset(GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Content.objects.all()
    serializer_class = CotentSerializer

'''退出登录'''
class Logoutview(APIView):
    def post(self, request):
        print(request.user,'退出')
        logout(request)
        return Response({'code': 200, 'msg': '退出登录成功！'})


class Register(APIView):
    authentication_classes = (BasicAuthentication, CsrfExemptSessionAuthentication)

    def post(self, request):
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            return Response({'code': 400, 'data': '用户已存在'})
        else:
            return Response({'code': 200, 'data': '用户名可用'})
