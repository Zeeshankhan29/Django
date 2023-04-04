from django.shortcuts import render
from django.http import HttpResponse
import pymongo
# Create your views here.


def test(request):
    return render(request,'base.html')