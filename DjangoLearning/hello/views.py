from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    return render(request,"hello/index.html")

def manish(request):
    return HttpResponse("Hello, Manish")

def David(request):
    return HttpResponse("Hello, David")

def greet(request,name):
    # return HttpResponse(f"Hello,{name}")
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })