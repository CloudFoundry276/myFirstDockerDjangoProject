from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first_view(request):
    return HttpResponse("I am the creator of my destiny")
