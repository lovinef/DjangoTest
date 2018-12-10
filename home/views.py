from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    msg = 'My Message'
    return render(request, 'home/index.html', {'message' : msg})