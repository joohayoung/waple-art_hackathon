from django.shortcuts import render

# Create your views here.
def sign_up(request):
    return

def login(request):
    return render(request, 'accountapp/login.html')

def logout(request):
    return