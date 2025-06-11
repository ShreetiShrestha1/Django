from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
    return HttpResponse("Hello! This is my first jango app")



def country(request):
    context ={
        "country_name" : "Nepal",
        "continent" : "Asia",
        "country_code":"+977"
    }
    return render(request,"country.html", context)

def province(request):
    context ={
        "province_name" : "Bagmati" ,
        "province_code" : "008"
    }
    return render(request,"province.html", context)

def Try(request):
    return render(request,"Try.html")