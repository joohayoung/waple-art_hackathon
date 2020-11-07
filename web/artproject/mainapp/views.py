from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'mainapp/home.html')

@login_required(login_url='/accountapp/login')
def map(request):
    context={}
    postlist = Post.objects.filter(user = request.user)
    imageitem = postlist.exclude(image = '')
    # print(imageitem)
    # if postlist:
    Seoul = imageitem.filter(country = '서울').order_by('-date').first()
    Busan = imageitem.filter(country = '부산').order_by('-date').first()
    Gwangju = imageitem.filter(country = '광주').order_by('-date').first()
    Ulsan = imageitem.filter(country = '울산').order_by('-date').first()
    Daegu = imageitem.filter(country = '대구').order_by('-date').first()
    Daejeon = imageitem.filter(country = '대전').order_by('-date').first()
    Incheon = imageitem.filter(country = '인천').order_by('-date').first()

    GG = imageitem.filter(country = '경기도').order_by('-date').first()
    GW = imageitem.filter(country = '강원도').order_by('-date').first()
    CN = imageitem.filter(Q(country = '충청남도')|Q(country='세종시')).order_by('-date').first()
    CB = imageitem.filter(country = '충청북도').order_by('-date').first()
    GB = imageitem.filter(country = '경상북도').order_by('-date').first()
    JB = imageitem.filter(country = '전라북도').order_by('-date').first()
    GN = imageitem.filter(country = '경상남도').order_by('-date').first()
    JN = imageitem.filter(country = '전라남도').order_by('-date').first()
    Jeju = imageitem.filter(country = '제주도').order_by('-date').first()
    
    context['list'] = {'Seoul':Seoul, 'Busan':Busan, 'Gwangju':Gwangju, 'Ulsan':Ulsan, 'Daegu':Daegu, 'Daejeon':Daejeon, 'Incheon':Incheon,
                        'GG':GG, 'GW':GW, 'CN':CN, 'CB':CB, 'GB':GB, 'JB':JB, 'GN':GN, 'JN':JN, 'Jeju':Jeju}
    context['postlist'] = postlist # real 게시물 전체 복록
    print(context['list'])
    return render(request, 'mainapp/map.html', context)

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'mainapp/posting.html', {'post':post})

@login_required(login_url='/accountapp/login')
def upload(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            new_article=Post.objects.create(
                user = request.user,
                name=request.POST['name'],
                comment=request.POST['comment'],
                image=request.FILES['image'],
                rating=request.POST['rating'],
                # item=request.POST['item'],
                item = "전시회",
                date=request.POST['date'],
                country=request.POST['country'],
                city=request.POST['city'],
            )
        else:
            new_article=Post.objects.create(
                user = request.user,
                name=request.POST['name'],
                comment=request.POST['comment'],
                rating=request.POST['rating'],
                # item=request.POST['item'],
                item = "전시회",
                date=request.POST['date'],
                country=request.POST['country'],
                city=request.POST['city'],
            )
        return redirect('mainapp:map')
    return render(request, 'mainapp/upload.html')

@login_required(login_url='/accountapp/login')
def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('mainapp:map')
    return render(request, 'mainapp/remove_post.html', {'Post': post})

@login_required(login_url='/accountapp/login')
def RegionPostList(request, num):
    postlist = Post.objects.filter(user = request.user)
    context={}
    if num == 1:
        postlist = postlist.filter(country = '서울').order_by('-date')
        region = '서울'
    elif num == 2:
        postlist = postlist.filter(country = '부산').order_by('-date')
        region = '부산'
    elif num == 3:
        postlist = postlist.filter(country = '광주').order_by('-date')
        region = '광주'
    elif num == 4:
        postlist = postlist.filter(country = '울산').order_by('-date')
        region = '울산'
    elif num == 5:
        postlist = postlist.filter(country = '대구').order_by('-date')
        region = '대구'
    elif num == 6:
        postlist = postlist.filter(country = '대전').order_by('-date')
        region = '대전'
    elif num == 7:
        postlist = postlist.filter(country = '인천').order_by('-date')
        region = '인천'
    elif num == 8:
        postlist = postlist.filter(country = '경기도').order_by('-date')
        region = '경기도'
    elif num == 9:
        postlist = postlist.filter(country = '강원도').order_by('-date')
        region = '강원도'
    elif num == 10:
        postlist = postlist.filter(country = '충청남도').order_by('-date')
        region = '충청남도'
    elif num == 11:
        postlist = postlist.filter(country = '충청북도').order_by('-date')
        region = '충청북도'
    elif num == 12:
        postlist = postlist.filter(country = '경상북도').order_by('-date')
        region = '경상북도'
    elif num == 13:
        postlist = postlist.filter(country = '전라북도').order_by('-date')
        region = '전라북도'
    elif num == 14:
        postlist = postlist.filter(country = '경상남도').order_by('-date')
        region = '경상남도'
    elif num == 15:
        postlist = postlist.filter(country = '전라남도').order_by('-date')
        region = '전라남도'
    elif num == 16 : #16
        postlist = postlist.filter(country = '제주도').order_by('-date')
        region = '제주도'
    else :
        postlist = postlist.order_by('-date')
        region = '전체'

    context['region'] = region
    context['postlist'] = postlist
    return render(request, 'mainapp/RegionPostList.html', context)

def edit_posting(request):
    return render(request, 'mainapp/edit_posting.html')