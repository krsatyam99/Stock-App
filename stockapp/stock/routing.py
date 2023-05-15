# from django.urls import re_path

# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/stocks/(?P<room_name>\w+)/$', consumers.StocksConsumer.as_asgi()),
# ]
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path
from stock import consumers

# from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/stocks/(?P<room_name>\w+)/$', consumers.StocksConsumer.as_asgi()),
    re_path(r'ws/stocks/$', consumers.StocksConsumer.as_asgi()),
]
