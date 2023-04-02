from rest_framework.response import Response
from rest_framework.decorators import api_view
from pathlib import Path
import socketio

# Build paths inside the project like this: BASE_DIR / 'subdir'.
ASYNC_MODE = 'gevent'
BASE_DIR = Path(__file__).resolve().parent.parent


sio = socketio.Server(async_mode=ASYNC_MODE)


@api_view(["GET", "POST", "PUT", "DELETE"])
def index(req):
    if (req.method == "GET"):
        sio.emit("notification", data={"data": {"title": req.GET.get(
            "title"), "content": req.GET.get("content")}})
        return Response({"data": "hello"}, status=200)


@sio.event
def connect(sid, environ):
    """ Programme de connexion
        Au cour de la connexion, on enregistre tous les utilisateurs
        connectes
    """
    print(f"{sid}\t has been connected")


@sio.event
def disconnect(sid):
    """ Programme de deconnexion
        Lors de la deconnexion, on supprime l'utilisateur de la liste des
        connectes
    """
    print(f"user disconnected")
