from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from api.consumers import ContentListConsumer, ContentDetailConsumer


application = ProtocolTypeRouter({

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^api/$", ContentListConsumer),
            url(r"^api/<pk>/$", ContentDetailConsumer),
        ])
    ),
})