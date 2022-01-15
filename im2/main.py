import socketio,django,os
import eventlet  # 协程
import sys
# 获取启动命令中的参数 sys.argv = ['server.py',[port]]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.extend([BASE_DIR,])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "background_app.settings")
# 将所有用到的系统标准io函数替换成eventlet提供的同名函数
eventlet.monkey_patch()
# django.setup()

import eventlet.wsgi
# 创建sio服务器

import server
# if len(sys.argv) < 2:
#     print('未提供端口号')
#     exit(1)
# port = int(sys.argv[1])
import chat
port=5000
# 写死
#SERVER_ADDRESS = ('',8000)

# 启动中指定端口号

SERVER_ADDRESS = ('0.0.0.0',port)
# 创建协程服务器 并启动
sock = eventlet.listen(SERVER_ADDRESS,)
#启动协程服务器
eventlet.wsgi.server(sock, server.app)
