
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request):
    # request.session.clear()
    if (not request.session.has_key('id')):
        request.session['id'] = 0
    else:
        request.session['id'] += 1
    data={"number": request.session['id'].__str__}
    return render(request, "home/index.html", data, status=200)

