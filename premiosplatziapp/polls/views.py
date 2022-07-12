from django.shortcuts import render
from django.http import HttResponse

def index(request):
    return HttResponse("Hello World")
