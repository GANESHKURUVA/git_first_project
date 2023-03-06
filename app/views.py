from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ganesh(request):
    return HttpResponse("<marquee><span color='yellow'><h1>☆*: .｡. o(≧▽≦)o .｡.:*☆GANESH☆*: .｡. o(≧▽≦)o .｡.:*☆</h1></span></marquee>")


def gani(request):
    return HttpResponse("<h1><span style:color:yellow>unmannede vihicle no one can touch</span> </h1>")