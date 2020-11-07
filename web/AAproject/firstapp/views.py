from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    return render(request, 'firstapp/home.html', context)

def result(request):
    context={}
    return render(request, 'firstapp/result.html', context)