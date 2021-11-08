from django.contrib.auth import login, authenticate

from main.userserializer import UserSerializer

from main.views import UserinfoViewset


def my_jwt_response_payload_handler(token, user, request):
    info = UserSerializer(user)
    login(request,user)

    return {
            'code': 200,
            'token': token,
            'data': info.data,
        }
