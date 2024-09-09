from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')
def continue_view(request):
    return render(request, 'continue.html')