from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1><marquee>Virat is king of cricket</marquee></h1>')
def abd(request):
    return render(request,'abd.html')