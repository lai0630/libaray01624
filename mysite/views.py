from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post,Mood,Comment
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django import forms as LoginForm
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from django.utils.text import slugify
from mysite.forms import CommentForm

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
		return redirect('/')

def log(request):
	return render(request, 'login.html')

def book_list(request):
    books = Post.objects.all()
    return render(request, 'book_list.html', {'books': books})

	
def borrow_book(request, book_id):
    book = get_object_or_404(Post, id=book_id)

    if not book.isBorrow:
        book.isBorrow = True
        book.save()

    return HttpResponseRedirect(reverse('book_list'))

def return_book(request, book_id):
    book = get_object_or_404(Post, id=book_id)

    if book.isBorrow:
        book.isBorrow = False
        book.save()

    return HttpResponseRedirect(reverse('book_list'))

def search(request):
    kw = request.GET.get('q')#抓表單的東西(看你header的名字)
    posts = Post.objects.filter(title__icontains=kw)#title__icontains相似查詢
    return render(request, 'search.html', {'posts': posts, 'keyWord': kw})

from django.shortcuts import render

def forms(request):#用這種
    if request.method == 'GET':
        form = CommentForm()
        posts = Comment.objects.filter(enabled=True).order_by('-pub_time')[:30]
        return render(request,'myform.html',locals())#一定要回應
    elif request.method =='POST':
        form = CommentForm(request.POST)#去request抓資料 把變數抓下來
        posts = Comment.objects.filter(enabled=True).order_by('-pub_time')[:30]
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            form.save()  #這邊可以存是因為他在forms已經定義好了 不然要像18 19那行
        return render(request,'myform.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'myform.html',locals())#一定要回應
