from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_view(request):
    return HttpResponse("My first docker django project with Docker Compose and Volumes")
