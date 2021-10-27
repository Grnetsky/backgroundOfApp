
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        '''认知逻辑'''
        #如果认知失败抛出AuthencationFailed
        token = request.query_params.get('token')
        if token:
            user_token = User
        else:
            raise AuthenticationFailed("需要携带token")

        return user,token # 返会两个值，若有多个认证，则返会两个值的类放到最后


from rest_framework.permissions import BasePermission
class UserPermission(BasePermission):
    def has_permission(self, request, view):
        #不是超级用户不让访问
        #由于已经认证过了，request中有user对象了
        user = request.user
        if user.user_type ==1:
            print(user.get_user_type_display())  #若字段中有choose 则用get_字段名_display()来获取对应的详情
            return True
        else:
            return False

