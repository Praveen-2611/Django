from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1><marquee><h1><marquee>Virat is best batmen in tha world</h1></marquee>')