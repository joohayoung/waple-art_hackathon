from django.shortcuts import render
from .models import ArtInfoDB, PerformanceDB, FestivalDB, ArtWorkDB
from django.db.models import Q, Count
# Create your views here.

def test(request):
    return render(request, 'subapp/test.html')

def search(request):
    return render(request, 'subapp/search.html')

def result(request):
    context={}
    # 키워드 검색
    if request.method == "GET":
        kw = request.GET.get('kw', '')
        context['kw'] = kw

        #정렬(나중에 추가)
        contents = ArtInfoDB.objects.all()

        #키워드 검색
        if kw !='': #키워드 입력이 들어왔을때
            contents = contents.filter(
                Q(title__contains=kw) | Q(host__contains=kw)|
                Q(region__contains=kw) | Q(category__contains=kw)
            ).distinct()
        else:
            pass #키워드 검색 안되면 전체

        context['contents'] = contents
    return render(request, 'subapp/result.html', context)

def detail(request, content_pk):
    context={}

    content = PerformanceDB.objects.get(basic_title=content_pk)
    if content == False : 
        content = FestivalDB.objects.get(pk=content_pk)
    if content == False :
        content = ArtWorkDB.objects.get(pk=content_pk)

    context['content'] = content
    return render(request, 'subapp/detail.html', context)