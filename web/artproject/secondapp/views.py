from django.shortcuts import render
from .models import PlaceDB
from accountapp.models import info
from django.db.models import Q, Count
from graph_output.main import outputpredictor
# Create your views here.

def place_search(request):
    context={}
    results=None
    region = None
    age = None
    gender = None
    kw=''

    if request.method == "GET":
        kw = request.GET.get('kw', '')
        if kw != '':
            results = PlaceDB.objects.filter(
                Q(title__contains=kw) | Q(address__contains=kw)
            )
        else:
            results = PlaceDB.objects.all()

        myinfo = request.GET.get('myinfo', 'no')
        if myinfo == 'yes':
            if request.user.is_authenticated: # 요청을 보낸 유저가 로그인한 상태일 경우
                userinfo = info.objects.get(user_id = request.user)
                region = userinfo.region
                gender = userinfo.gender
                if gender=="여성" : gender="woman"
                else : gender="man"
                age = userinfo.age
                if age>=0 and age<10 : age = 0
                elif age >=10 and age<20 : age = "10"
                elif age >=20 and age<30 : age = "20"
                elif age >=30 and age<40 : age = "30"
                elif age >=40 and age<50 : age = "40"
                elif age >=50 and age<60 : age = "50"
                else: age = 60
            else:
                region = 'all'
                gender = 'all'
                age = 'all'
                context['error'] = True
        
        else:
            region = request.GET.get('region', 'all')
            gender = request.GET.get('gender', 'all')
            age = request.GET.get('age', 'all')

        # 페이지를 고민하자
        # 지역필터링
        if region == 'all':
            pass
        else:
            results = results.filter(region=region)

        #나이-성별 조건 처리
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
        # 고치기 #회원가입 보고
        # 로그인한 사용자일때 > 사용자 정보기준 상위 10개
        results = PlaceDB.objects.all().order_by('allsum')


    context['results'] = results
    # context['message'] = message
    context['region'] = region
    context['age'] = age
    context['gender'] = gender
    context['kw'] = kw

    return render(request, 'secondapp/place_search.html', context)

def place_detail(request, pk):
    context={}
    result = PlaceDB.objects.get(pk = pk)
    # 어차피 GET 요청만 들어온다
    # 이번주 통계 값 DB에서 불러오기
    # 0, 10, 20, 30, 40, 50, 60
    context['graph1_w'] = [result.kids_w, result.ten_w, result.twenty_w, result.thirty_w, result.forty_w, result.fifty_w, result.old_w]
    context['graph1_m'] = [result.kids_m, result.ten_m, result.twenty_m, result.thirty_m, result.forty_m, result.fifty_m, result.old_m]

    # 분석 값 가져오기
    age = request.GET.get('age', 'all') # 'all', 'man', 'woman'
    gender = request.GET.get('gender', 'all') # '0' '10''20'... '60'
    if age == "all":
        gender = 'all'
    title = result.title #'미술관이름~'

    graph2 = outputpredictor(age, gender, title)

    context['graph2'] = graph2 # [777, 800, 100, 75, 84, 338, 400 ]
    
    context['age'] = age
    context['gender'] = gender
    context['result'] = result
    context['pkk'] = pk
    return render(request, 'secondapp/place_detail.html', context)