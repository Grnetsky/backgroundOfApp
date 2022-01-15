from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from main.userserializer import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    '''
    token验证
    '''
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        info = UserSerializer(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['data'] = info.data
        data['code'] = 200
        return data


#     login(request,user)
#
#     return {
#             'code': 200,
#             'token': token,
#             'data': info.data,
#         }