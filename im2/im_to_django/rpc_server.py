import time
import grpc, os, django, sys
import im_to_django_pb2_grpc
import im_to_django_pb2
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.extend([BASE_DIR, ])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "background_app.settings")
django.setup()
from rest_framework_simplejwt.authentication import JWTAuthentication

from main.views import User
print("进入rpc服务器")

# 服务端事件处理函数
class nameServicer(im_to_django_pb2_grpc.nameServicer):
    """
    通过子类继承重写的方式
    """
    def tokrn_interface(self, request, context):
        """??rpc????????
        :param request: 调用时的请求参数对象 就是传值的时候传的那个对象
        :param context: 通过此对象，可以设置调用返回的异常信息
        """
        # 获取调用的参数，
        token = request.token
        token = token.strip('JWT ')
        try:
            token_back = JWTAuthentication().get_validated_token(str(token))
            user = User.objects.filter(id=token_back['user_id']).exists()
            user_id = token_back['user_id']
        except Exception as err:
            print(err)
            user = False

        response = im_to_django_pb2.req_data()
        if user:
            response.user_exist = True
            response.user_id = user_id

        else:
            response.user_exist = False
            response.user_id = 0
        # response.user_info = User.objects.get(id=23).sex
        # article_list = []
        # article = im_to_django_pb2.article()
        # article_list.append(article)
        # # 列表类型时使用extend()方法
        # 决定返回数据
        print(response.user_exist)
        return response
        # raise NotImplementedError('Method not implemented!')


# 创建rpc服务器
def serve():
    # 创建rpc服务器
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    # 将自己实现的调用方法和服务器绑定
    im_to_django_pb2_grpc.add_nameServicer_to_server(nameServicer(), server)
    server.add_insecure_port('127.0.0.1:8888')
    # 开启服务器,start方法是非阻塞方法
    server.start()
    # 防止程序退出
    while True:
        time.sleep(10)


if __name__ == '__main__':
    serve()
