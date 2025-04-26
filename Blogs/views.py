from django.shortcuts import render
from django.http import HttpResponse

def BlogsHomeView(request):
    return HttpResponse("Sudden Project`s Blogs Home")
