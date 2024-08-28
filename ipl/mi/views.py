from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rohit(request):
    return HttpResponse('<h1><marquee>rohit is best captain</marquee></h1>')
def hardik(request):
    return render(request,'hardik.html')