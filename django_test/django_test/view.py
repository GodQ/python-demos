from django.http import HttpResponse
from django.shortcuts import render
import datetime


# def hello(request):
#     return HttpResponse("Hello GodQ!")


def hello(request):
    now = datetime.datetime.now()
    data_list = [0, 1, 2, 3]
    context = {
        "time": now,
        "title": "hello Title!",
        "name": "hello GodQ Name:",
        "data_list": data_list
    }
    return render(request, 'show.html', context)


def raw_api(request):
    return HttpResponse("OK")