from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def register(request):
    return HttpResponse("Welcome to Visual Roll.")
def create_group(request):
    return HttpResponse("Welcome to Visual Roll.")