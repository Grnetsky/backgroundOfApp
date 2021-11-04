from django.contrib.auth import login, authenticate

from main.userserializer import UserSerializer

from main.views import UserinfoViewset


def my_jwt_response_payload_handler(token, user, request):
    usr = authenticate(username=request.data.get('username'), password=request.data.get('password'))
    info = UserSerializer(user)
    if not usr:
        return {
            'code': 404,
            'errmsg': '用户名密码错误'
        }
    else:
        login(request, user=usr)
        request.session.session_key
        print(request.user.username,'登录')
        return {
            'code': 200,
            'token': token,
            'data': info.data,
            'sessionid':request.session.session_key
        }
