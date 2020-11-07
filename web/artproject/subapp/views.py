from django.shortcuts import render
from .models import ArtInfoDB, PerformanceDB, FestivalDB
from django.db.models import Q, Count
# Create your views here.

def search(request):
    context={}
    start = None
    end = None
    category = None

    contents = ArtInfoDB.objects.all()
    # 키워드 검색
    kw = request.GET.get('kw', '')
    context['kw'] = kw
    if kw !='': #키워드 입력이 들어왔을때
        contents = contents.filter(
            Q(title__contains=kw) | Q(host__contains=kw)|
            Q(region__contains=kw) | Q(category__contains=kw)
        ).distinct()
    else :
        pass

    # 시간 필터링
    # start = request.GET.get('start', '')
    # end = request.GET.get('end', '')
    # context['start'] = start
    # context['end'] = end
    
    category = request.GET.get('category', 'all')
    context['category'] = category

    if category == 'festival' : 
        contents = contents.filter(category = '축제/행사')
    elif category == 'performance':
         contents = contents.filter(category = '공연/전시')
    else : 
        pass
        
    context['contents'] = contents
    return render(request, 'subapp/search.html', context)

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