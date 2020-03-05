from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .model_ import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import hashlib

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        input_data = JSONParser().parse(request)

        category = predict(input_data['input_url'])
        return JsonResponse({'category':category})

class Predictor(APIView):

    def post(self,request):
        input_data = JSONParser().parse(request)

        category = predict(input_data['input_url'])
        return Response({'category':category})
