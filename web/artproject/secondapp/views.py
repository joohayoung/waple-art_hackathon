from django.shortcuts import render

# Create your views here.
def search_place(request):
    return render(request, 'secondapp/search_place.html')

def result(request):
    return render(request, 'secondapp/search_place_result.html')

def place_detail(request):
    return render(request, 'secondapp/place_detail.html')