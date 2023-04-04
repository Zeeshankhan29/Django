from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test1(req):
    return HttpResponse('This is the second app')