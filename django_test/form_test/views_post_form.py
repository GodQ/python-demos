from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def search_form_post(request):
    return render(request, "search_form_post.html")


def search_post(request):
    request.encoding = 'utf-8'
    print(request.POST)
    if 'q' in request.POST:
        message = 'You are searching {}'.format(request.POST['q'])
    else:
        message = 'Error: Empty Form'
    return HttpResponse(message)

