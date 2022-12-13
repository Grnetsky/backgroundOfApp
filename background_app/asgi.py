"""
ASGI config for background_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from background_app import routing
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'background_app.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http":get_asgi_application(), # http请求
    "websocket":URLRouter(routing.websocket_urlpatterns)  # websocket请求
})
