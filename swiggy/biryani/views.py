from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def chickenbiryani(request):
    return HttpResponse('<h1><marquee>Best chicken biryani available here</marquee></h1>')
def vegbiryani(request):
    return render(request,'vegbiryani.html')