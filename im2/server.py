import socketio
import eventlet
import kombu

# 将所有用到的系统标准io函数替换成eventlet提供的同名函数

# from . import wsgi_app
fJWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'

# 连接rabbitmq
mgr = socketio.KombuManager("amqp://admin:admin@localhost:5672//")  # amqp://用户名:密码@localhost：5672/v_host名

sio = socketio.Server(logger=True, engineio_logger=True,async_mode="eventlet", client_manager=mgr,always_connect=True,cors_allowed_origins='*')

# 将socketio绑定到wsgi的app上
app = socketio.WSGIApp(sio)


# eventlet.wsgi.server(eventlet.listen((''
