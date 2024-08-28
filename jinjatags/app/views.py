from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'Praveen','age':22,'mbno':1234567890,'email':'something@gmail.com'}
    return render(request,'jinjatags.html',context=d)