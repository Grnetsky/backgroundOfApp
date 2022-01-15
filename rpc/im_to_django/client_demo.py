import grpc
import im_to_django_pb2_grpc
import im_to_django_pb2


def get_userinfo(stub):
    """
    调用rpc检查用户身份
    :return:
    """
    rsp_data = im_to_django_pb2.rsp_data()
    rsp_data.user_id = 23
    rsp_data.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNSwidXNlcm5hbWUiOiIxMTExMSIsImV4cCI6MTY3MzQ5MTc3MCwiZW1haWwiOiIifQ.OhTmRbltCyf0PeWeKPZRLRTMZQJ2IzIhy8oHnNKdHNw"
    res = stub.tokrn_interface(rsp_data)
    print(res)


def run():
    # 构建连接rpc服务器的对象
    with grpc.insecure_channel('127.0.0.1:8888') as channel:
        stub = im_to_django_pb2_grpc.nameStub(channel)
        # req = stub.tokrn_interface()
        get_userinfo(stub)


if __name__ == '__main__':
    run()
