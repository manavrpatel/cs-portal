from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<uuid:ticket_id>/', consumers.ChatConsumer.as_asgi()),
]