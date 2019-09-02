from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.views import View


class AppView(View):
    def get(self, request):
        return HttpResponse("Get")

    def post(self, request):
        return HttpResponse("Post")

    def delete(self, request):
        return HttpResponse("Delete")
