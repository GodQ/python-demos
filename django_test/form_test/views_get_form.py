from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def search_form_get(request):
    return render(request, "search_form_get.html")


def search_get(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = 'You are searching ' + request.GET['q']
    else:
        message = 'Error: Empty Form'
    return HttpResponse(message)

