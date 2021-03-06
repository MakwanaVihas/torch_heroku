from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .model_ import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):

    if request.method == "POST":
        input_data = JSONParser().parse(request)
        try:
            category = predict(input_data['input_url'])
            return JsonResponse({'category':category})
        except KeyError:
            return JsonResponse({'key-error':'Invalid Key'})
    return HttpResponse("MAKE POST REQUEST INSTEAD")

class Predictor(APIView):

    def post(self,request):
        input_data = JSONParser().parse(request)
        try:
            category = predict(input_data['input_url'])
            return Response({'category':category})
        except KeyError:
            return Response({'key-error':'Invalid Key'})
