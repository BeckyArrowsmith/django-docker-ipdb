from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    #import ipdb; ipdb.set_trace()
    return HttpResponse("Hello, world!")
