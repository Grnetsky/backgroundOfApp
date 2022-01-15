import socketio
import eventlet

# 将所有用到的系统标准io函数替换成eventlet提供的同名函数
# from . import wsgi_app
fJWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'

mgr = socketio.KombuManager("amqp://admin:admin@localhost:5672//",exchange_options={"type":"direct"})  # amqp://用户名:密码@localhost：5672/v_host名

sio = socketio.Server(logger=True, engineio_logger=True,async_mode="eventlet", client_manager=mgr,always_connect=True,cors_allowed_origins='*')
app = socketio.Middleware(sio)

# eventlet.wsgi.server(eventlet.listen((''
