# from django.contrib.auth import login, authenticate
#
# from main.userserializer import UserSerializer
#
# from main.views import UserinfoViewset
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
#
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         info = UserSerializer(user)
#         # Add custom claims
#         token['name'] = user.name
#         token['code'] = 200
#         token['data'] = info.data
#         return token
#
# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
#
# def my_jwt_response_payload_handler(token, user, request):
#     info = UserSerializer(user)
#     login(request,user)
#
#     return {
#             'code': 200,
#             'token': token,
#             'data': info.data,
#         }