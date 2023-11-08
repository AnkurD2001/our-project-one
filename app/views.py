from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def JamPandu(request):
    return HttpResponse('Hi JamPandu How are you')