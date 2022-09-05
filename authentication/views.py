from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hello(request):
    now = datetime.datetime.now()
    html = "<html><body><h2>It is now %s.</h2></body></html>" % now
    return HttpResponse(html)