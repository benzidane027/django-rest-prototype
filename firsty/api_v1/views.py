import stat
from unicodedata import name
from rest_framework.response import Response
from rest_framework.decorators import api_view
from PIL import Image
import json
from bson.json_util import dumps
from pathlib import Path
import os
from .models import Task
from django.core import serializers


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
#database = mongoClient["testy"]

# upload image from api




@api_view(["GET", "POST", "PUT", "DELETE"])
def index(req):
    if (req.method == "GET"):
        return Response({"data": Task.objects.all().values()}, status=200)
    elif (req.method == "POST"):
        obj = Task(content=req.POST.get("content"), date=req.POST.get("date"))
        obj.save()
        return Response({"data": ""}, status=200)
    elif (req.method == "PUT"):
        Task.objects.filter(date=req.POST.get("date")).update(
            content=req.POST.get("content"))
        return Response({"data": ""}, status=200)
    elif (req.method == "DELETE"):
        Task.objects.filter(date=req.POST.get("date")).delete()
        print(req.POST.get("date"))
        return Response({"data": ""}, status=200)
    else:
        return Response({"data": "error"}, status=400)


""" def index(request):
    try:
        mfile = request.FILES.get("mfile")
        im = Image.open(request.FILES["mfile"])
        im.save(os.path.join(BASE_DIR, "public", "upload_file") +
                "/"+str(mfile), quality=10, optimize=True)
        # print uuid.uuid4()
        return Response({"data": ""}, status=200)
    except:
        return Response({"data": ""}, status=400)
 """

# fetch and set data into mongodb
""" @api_view(["POST"])
def test01(request):
    collection = database["user"]
    # collection.insert_one({"name":"mohamed"})
    return Response({"data": json.loads(dumps(collection.find({})))}, status=200) """


# fetch and set data into model
""" @api_view(["POST"])
def test02(request):
    Testify.objects.filter(name="malik").delete()
    obj = Testify(
        name=request.POST.get("name"), age=55,
        maried=True,
        discription="",
        pic=request.FILES["mfile"]
    )
    obj.save()
    data = Testify.objects.filter().order_by("-id").values()
    return Response({"data": data}, status=200,)
 """
