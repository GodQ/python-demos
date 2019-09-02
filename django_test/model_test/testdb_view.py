from django.http import HttpResponse
from django.shortcuts import render
import datetime

from model_test.models import Test


def writedb(request):
    now = datetime.datetime.now()
    test = Test(name="name-{}".format(now))
    test.save()
    return HttpResponse("DB write successfully!")


def readdb(request):
    r = Test.objects.all()
    name_list = list()
    for line in r:
        name_list.append(line.name)
    context = {
        "title": "Read DB Result",
        "time": datetime.datetime.now(),
        "name": "Read DB Result",
        "data_list": name_list
    }
    return render(request, "show.html", context)


def updatedb(request):
    test = Test.objects.get(id=1)
    test.name = "GodQ1-{}".format(datetime.datetime.now())
    test.save()
    Test.objects.filter(id=2).update(name="GodQ2-{}".format(datetime.datetime.now()))
    return HttpResponse("Update DB successfully!")
