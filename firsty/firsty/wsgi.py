"""
WSGI config for firsty project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firsty.settings')

#use this line for not using socketio
django_asgi_app=get_wsgi_application()

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from socketioTest.views import sio
import socketio

application = socketio.WSGIApp(sio, django_asgi_app);


server = pywsgi.WSGIServer(("", 8000), application, handler_class=WebSocketHandler);
server.serve_forever()
