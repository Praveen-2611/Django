from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1><marquee>Dhoni is best wicket keeper in the world</h1></marquee>')