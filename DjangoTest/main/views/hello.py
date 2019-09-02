from django.http import JsonResponse


def hello(request):
    return JsonResponse({"code": 200, "msg": "OK"})

