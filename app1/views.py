from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chandu(request):
    return HttpResponse('<h1> chandu is a good boy </h1>')
def gaye(request):
        return HttpResponse('<h1><marquee>gaye is a very talktive girl</h1></marquee>') 