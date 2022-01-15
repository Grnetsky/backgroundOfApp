# shij事件处理函数
# 设置环境变量中的 DJANGO_SETTINGS_MODULE 设置为 django 配置
# 启动 django 配置、注册 app 等等初始化操作
from django.core.handlers.wsgi import WSGIRequest
from server import sio
import time
import grpc
from im_to_django import im_to_django_pb2_grpc
from im_to_django import im_to_django_pb2

print("运行socketio")


def get_userinfo(stub, token):
    """
    调用rpc检查用户身份
    :return:
    """
    rsp_data = im_to_django_pb2.rsp_data()
    rsp_data.token = token
    res = stub.tokrn_interface(rsp_data)
    print(res)
    return res


def check_user_exist(token):
    # 构建连接rpc服务器的对象
    with grpc.insecure_channel('127.0.0.1:8888') as channel:
        stub = im_to_django_pb2_grpc.nameStub(channel)
        # req = stub.tokrn_interface()
        return get_userinfo(stub, token)


USER_LIST = []


@sio.on('connect')
def on_connect(sid, environ):
    request = WSGIRequest(environ)
    """
    在客户端连接之后被执行
    :param sid：string 客户端设置的用户id
    :environ :http请求数据
    :return:
    """
    print(request.headers)
    token = request.headers.get("token")
    print(token)
    back_data = check_user_exist(token)
    # 向客户端发送事件消息
    msg_data = {
        'msg': 'hello',
        'timestamp': round(time.time() * 1000)
    }
    print(back_data.user_exist)
    if back_data.user_exist:
        sio.enter_room(sid, room=str(back_data.user_id))
        if str(back_data.user_id) in USER_LIST:
            pass
        else:
            USER_LIST.append(str(back_data.user_id))

        print(USER_LIST)
        sio.send({"message":"登陆成功"}, room=str(back_data.user_id))

    else:
        sio.disconnect(sid)
    # 多事件名称为message则可以直接调用 sio.send(msg_data, room=sid)


# 聊天时使用message事件 传输的聊天格式为json
@sio.on("chat")
def chat(sid, data):
    data_to = data["to"]
    data_from = data["from"]
    message = data["message"]
    data_type = data["type"]
    msg_data = {
        "from":data_from,
        "message": message,
        "sendtime": time.time(),
        "type":data_type
    }
    # sio.enter_room(sid=sid, room="we")
    # print(sio.rooms(sid))
    print(USER_LIST)
    user_online(data_to)
    sio.emit("chat",data=msg_data, room=str(data_to))
def user_online(user_id):
    while str(user_id) not in USER_LIST:
        time.sleep(0)
    return True
@sio.on("enter_room")
def enter_room(sid, data):
    data_obj = data
    print(data_obj)
    sio.enter_room(sid, room=data_obj["room"])
    sio.emit("message", data={"msg": "进入房间成功"}, room=sid)



@sio.on("disconnect")
def disconnect(sid):
    rooms = sio.rooms(sid)
    print(sid,"断开了连接")
    print(sio.rooms(sid))
    USER_LIST.remove(sio.rooms(sid)[1])
    for room in rooms:
        sio.leave_room(sid, room)
