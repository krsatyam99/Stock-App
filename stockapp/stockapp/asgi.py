# # """
# # ASGI config for stockproject project.

# # It exposes the ASGI callable as a module-level variable named ``application``.

# # For more information on this file, see
# # https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
# # """

# # import os

# # from channels.routing import ProtocolTypeRouter, URLRouter
# # from django.core.asgi import get_asgi_application

# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockapp.settings')

# # # Needed if starting server using daphne or uvicorn command
# # import django
# # django.setup()

# # from channels.auth import AuthMiddlewareStack
# # # from stock.routing import websocket_urlpatterns
# # from stock.routing import websocket_urlpatterns

# # application = ProtocolTypeRouter({
# #     "http": get_asgi_application(),
# #     # Just HTTP for now. (We can add other protocols later.)
# #     "websocket": AuthMiddlewareStack(
# #         URLRouter(
# #             websocket_urlpatterns
# #         )
# #     ),
# # })
# """
# ASGI config for stockproject project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
# """

# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application

# from stock.routing import websocket_urlpatterns
# import django
# django.setup()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockapp.settings')

# # Needed if starting server using daphne or uvicorn command


# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             websocket_urlpatterns
#         )
#     ),
# })
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockapp.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import stock.routing
from stock.routing import websocket_urlpatterns



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            stock.routing.websocket_urlpatterns
        )
    ),
})

