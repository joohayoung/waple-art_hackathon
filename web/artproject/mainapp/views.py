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
    postlist = Post.objects.all()
    # context['postlist'] = postlist
    postlist = postlist.filter(user = request.user)

    # if postlist:
    Seoul = postlist.filter(country = '서울').order_by('-date').first()
    Busan = postlist.filter(country = '부산').order_by('-date').first()
    Gwangju = postlist.filter(country = '광주').order_by('-date').first()
    Ulsan = postlist.filter(country = '울산').order_by('-date').first()
    Daegu = postlist.filter(country = '대구').order_by('-date').first()
    Daejeon = postlist.filter(country = '대전').order_by('-date').first()
    Incheon = postlist.filter(country = '인천').order_by('-date').first()

    GG = postlist.filter(country = '경기도').order_by('-date').first()
    GW = postlist.filter(country = '강원도').order_by('-date').first()
    CN = postlist.filter(Q(country = '충청남도')|Q(country='세종시')).order_by('-date').first()
    CB = postlist.filter(country = '충청북도').order_by('-date').first()
    GB = postlist.filter(country = '경상북도').order_by('-date').first()
    JB = postlist.filter(country = '전라북도').order_by('-date').first()
    GN = postlist.filter(country = '경상남도').order_by('-date').first()
    JN = postlist.filter(country = '전라남도').order_by('-date').first()
    Jeju = postlist.filter(country = '제주도').order_by('-date').first()
    
    # else:
    #     Seoul = None
    #     Busan = None
    #     Gwangju = None
    #     Ulsan = None
    #     Daegu = None
    #     Daejeon = None
    #     Incheon = None

    #     GG = None
    #     GW = None
    #     CN = None
    #     CB = None
    #     GB = None
    #     JB = None
    #     GN = None
    #     JN = None
    #     Jeju = None
    context['list'] = {'Seoul':Seoul, 'Busan':Busan, 'Gwangju':Gwangju, 'Ulsan':Ulsan, 'Daegu':Daegu, 'Daejeon':Daejeon, 'Incheon':Incheon,
                        'GG':GG, 'GW':GW, 'CN':CN, 'CB':CB, 'GB':GB, 'JB':JB, 'GN':GN, 'JN':JN, 'Jeju':Jeju}

    # context['Seoul'] = Seoul
    # context['Busan'] = Busan
    # context['Gwangju'] = Gwangju
    # context['Ulsan'] = Ulsan
    # context['Daegu'] = Daegu
    # context['Daejeon'] = Daejeon
    # context['Incheon'] = Incheon

    # context['GG'] = GG
    # context['GW'] = GW
    # context['CN'] = CN
    # context['CB'] = CB
    # context['GB'] = GB
    # context['JB'] = JB
    # context['GN'] = GN
    # context['JN'] = JN
    # context['Jeju'] = Jeju

    context['postlist'] = postlist

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
                item=request.POST['item'],
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
                item=request.POST['item'],
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