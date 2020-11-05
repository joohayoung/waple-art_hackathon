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
    Aitem = None
    Bitem = None
    contentt = ArtInfoDB.objects.get(pk = content_pk)

    if contentt.category == '공연/전시' : 
        Aitem = PerformanceDB.objects.get(artinfo_id=content_pk)
    elif contentt.category == '축제/행사':
        Bitem = FestivalDB.objects.get(artinfo_id=content_pk)
    else : #'미술작품/건축물'
        item = ArtWorkDB.objects.get(artinfo_id=content_pk)

    context['Aitem'] = Aitem
    context['Bitem'] = Bitem
    return render(request, 'subapp/detail.html', context)