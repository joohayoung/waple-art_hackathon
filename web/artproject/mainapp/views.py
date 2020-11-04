from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    postlist = Post.objects.all()
    return render(request, 'mainapp/home.html', {'postlist':postlist})

def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'mainapp/posting.html', {'post':post})

@login_required
def upload(request):
    if request.method == 'POST':
        if request.POST['image']:
            new_article=Post.objects.create(
                name=request.POST['name'],
                comment=request.POST['comment'],
                image=request.POST['image'],
                rating=request.POST['rating'],
                item=request.POST['item'],
                date=request.POST['date'],
                country=request.POST['country'],
                city=request.POST['city'],
            )
        else:
            new_article=Post.objects.create(
                name=request.POST['name'],
                comment=request.POST['comment'],
                image=request.POST['image'],
                rating=request.POST['rating'],
                item=request.POST['item'],
                date=request.POST['date'],
                country=request.POST['country'],
                city=request.POST['city'],
            )
        return redirect('/')
    return render(request, 'mainapp/upload.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'mainapp/remove_post.html', {'Post': post})