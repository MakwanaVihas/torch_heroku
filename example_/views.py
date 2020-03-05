from django.shortcuts import render
from django.http import HttpResponse
import torch
import torchvision
# Create your views here.

def index(request):
    return HttpResponse(torchvision.__version__)
