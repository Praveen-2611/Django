from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(request):
    return HttpResponse('<h1><marquee>msd is cool captain</marquee></h1>')
def jadeja(request):
    return render(request,'jadeja.html')