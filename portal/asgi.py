import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import customer_support.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            customer_support.routing.websocket_urlpatterns
        )
    )
})
