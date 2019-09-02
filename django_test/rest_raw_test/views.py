from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

from .serializers import TestSerializer


# Create your views here.
class TestView(views.APIView):
    def get(self, request):
        arg1 = request.query_params.get('name')
        data = [
            {
                'name': arg1
            },
            {
                'name': 2
            }]
        results = TestSerializer(data, many=True).data
        return Response(results)
