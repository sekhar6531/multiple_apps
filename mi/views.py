from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return render(request,'rohit.html')

def bumrah(request):
    return HttpResponse('Boom Boom Bumrah')