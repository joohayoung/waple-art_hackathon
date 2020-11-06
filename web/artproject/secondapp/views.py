from django.shortcuts import render
from .models import PlaceDB
from django.db.models import Q, Count
# Create your views here.

def place_search(request):
    context={}
    results=None
    region = None
    age = None
    gender = None

    if request.method == "GET":
        print("GET 요청")
        #일단 10개를 보여주고 페이지를 고민하자
        # 지역필터링
        region = request.GET.get('region', 'all')
        if 'all' in region:
            results = PlaceDB.objects.all()
        else:
            results = PlaceDB.objects.filter(region=region)

        #중복 조건 처리
        gender = request.GET.get('gender', 'all')
        age = request.GET.get('age', 'all')

        if gender == 'woman':
            if age == '10':
                results = results.order_by('-ten_w')
            elif age == '20' : 
                results = results.order_by('-twenty_w')
            elif age == '30' : 
                results = results.order_by('-thirty_w')
            elif age == '40' : 
                results = results.order_by('-forty_w')
            elif age == '50' : 
                results = results.order_by('-fifty_w')
            elif age == '60' : 
                results = results.order_by('-old_w')
            elif age == '0' : #10대미만
                results = results.order_by('-kids_w')
            else : #all
                results = results.annotate(
                    allcount = Count("kids_w") + Count("ten_w") + Count("twenty_w")
                    + Count("thirty_w") + Count("forty_w") + Count("fifty_w") + Count("old_w")
                ).order_by('-allcount')
        elif gender == 'man':
            if age == '10':
                results = results.order_by('-ten_m')
            elif age == '20' : 
                results = results.order_by('-twenty_m')
            elif age == '30' : 
                results = results.order_by('-thirty_m')
            elif age == '40' : 
                results = results.order_by('-forty_m')
            elif age == '50' : 
                results = results.order_by('-fifty_m')
            elif age == '60' : 
                results = results.order_by('-old_m')
            elif age == '0' : #10대미만
                results = results.order_by('-kids_m')
            else : #all
                results = results.annotate(
                    allcount = Count("kids_m") + Count("ten_m") + Count("twenty_wm")
                   + Count("thirty_m") + Count("forty_m") + Count("fifty_m") + Count("old_m")
                ).order_by('-allcount')
        else: #gender = all
            if age == '10':
                results = results.annotate(
                    agecount = Count("ten_m") + Count("ten_w")
                ).order_by('-agecount')
            elif age == '20' : 
                results = results.annotate(
                    agecount = Count("twenty_m") + Count("twenty_w")
                ).order_by('-agecount')
            elif age == '30' : 
                results = results.annotate(
                    agecount = Count("thirty_m") + Count("thirty_w")
                ).order_by('-agecount')
            elif age == '40' : 
                results = results.annotate(
                    agecount = Count("forty_m") + Count("forty_w")
                ).order_by('-agecount')
            elif age == '50' : 
                results = results.annotate(
                    agecount = Count("fifty_m") + Count("fifty_w")
                ).order_by('-agecount')
            elif age == '60' : 
                results = results.annotate(
                    agecount = Count("old_m") + Count("old_w")
                ).order_by('-agecount')
            elif age == '0' : #10대미만
                results = results.annotate(
                    agecount = Count("kids_m") + Count("kids_w")
                ).order_by('-agecount')
            else : 
                pass # 그냥 그대로 전체

    else:
        # 고치기
        # 로그인한 사용자일때 > 사용자 정보기준 상위 10개
        results = PlaceDB.objects.all().order_by('allsum')


    context['results'] = results
    # context['message'] = message
    context['region'] = region
    context['age'] = age
    context['gender'] = gender

    return render(request, 'secondapp/place_search.html', context)

def place_detail(request, pk):
    context={}
    result = PlaceDB.objects.get(pk = pk)
    context['result'] = result
    return render(request, 'secondapp/place_detail.html', context)