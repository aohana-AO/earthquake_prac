from django.shortcuts import render
# Create your views here.
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View
from .models import Earthquake


def index(request):
    Earthquake_all = Earthquake.objects.all()
    return render(request,'index.html',{'Earthquake_all': Earthquake_all})


@ensure_csrf_cookie
def jsonget(request):
    if request.method == 'GET':
        return JsonResponse({})

    # JSON文字列
    datas = json.loads(request.body)

    Earthquake.objects.create(text=datas)

    # JSONに変換して戻す
    return JsonResponse(datas)
