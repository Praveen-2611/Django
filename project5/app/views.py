from django.shortcuts import render

# Create your views here.
def max(request):
    p={'a':100,'b':200,'c':300}
    return render(request,'max.html',p)