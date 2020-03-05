from django.shortcuts import render
from django.http import HttpResponse
import torch
# Create your views here.

def index(request):
    return HttpResponse(torch.__version__)
