from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post,Mood,Comment,Profile,BorrowingRecord
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django import forms as LoginForm
from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse
from django.utils.text import slugify
from mysite.forms import CommentForm,UserRegisterForm,LoginForm,ProfileForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

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
    if request.user.is_active:
        book = Post.objects.get(id=book_id)
        if book!=book.isBorrow:
            due_date = timezone.now() + timezone.timedelta(days=90)
            borrowing_record = BorrowingRecord.objects.create(
                user=request.user, 
                book=book,
                borrowing_date=timezone.now(),
                is_returned=False, 
            )
            book.isBorrow=True
            book.save()
            return render(request, 'borrowBook.html', {'borrowing_record': borrowing_record,'msg':'借閱成功！'})
        else:
            return render(request, 'borrowBook.html', {'msg': '圖書暫不可借'})
    else:
        messages.warning(request, '尚未登入不可借書，請先登入')
        return redirect('login')

    return HttpResponseRedirect(reverse('book_list'))

def return_book(request, book_id):
    if request.method=='POST':
        u=None
        returnCorrect=[]
        returnBookList=request.POST.getlist('return_books')
        for recordingId in returnBookList:
            recording=BorrowingRecord.objects.get(id=recordingId)
            recording.is_returned=True
            recording.actual_return_date=timezone.now()
            returnCorrect.append(recording)
            recording.save()

            recording.book.isBorrow=False
            recording.book.save()
            u=recording.user
        return render(request, 'returnBook.html',{'returnCorrect':returnCorrect,
                                                  'u':u})
    else:
        return redirect('/')   

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
            form = CommentForm()
        return render(request,'myform.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'myform.html',locals())#一定要回應
    
def register(request):#會直接存到這個程式的資料庫 而不是admin
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request,'register.html',locals())#一定要回應
    elif request.method =='POST':
        form = UserRegisterForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']
            user_password_confirm = form.cleaned_data['user_password_confirm']
            if user_password == user_password_confirm:
                user = User.objects.create_user(user_name,user_email,user_password)#有名字email password 密碼會加密
                message=f'註冊成功'
            else:
                message=f'兩次密碼不一樣'
        return render(request,'register.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'register.html',locals())#一定要回應
    
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def login (request):
    if request.method == 'GET':
        form = LoginForm()#代表會顯示的欄位 在forms那邊
        return render(request,'login.html',locals())#一定要回應
    elif request.method =='POST':
        form = LoginForm(request.POST)#去request抓資料 把變數抓下來
        if form.is_valid():#一定要寫這個(if以下的) 這個是要抓裡面的值
            user_name = form.cleaned_data['user_name']
            user_password = form.cleaned_data['user_password']
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("success")
                    message='成功'
                    return redirect('/')
                else:
                    message='未啟用'
            else:
                message='失敗'
        return render(request,'login.html',locals())#一定要回應
    else:
        massge='ERROR'
        return render(request,'login.html',locals())#一定要回應

@login_required(login_url='/login/') 
def profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.username
            try:
                user = User.objects.get(username=username)
                userinfo = Profile.objects.get(user=user)
                form = ProfileForm(instance=userinfo)
            except:
                form = ProfileForm()
        return render(request, 'userinfo.html', locals())
    elif request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            userinfo = Profile.objects.get(user=user)
            form = ProfileForm(request.POST, instance=userinfo)
            form.save()
            message = f'成功更新個人資料！'
        except:
            form = ProfileForm(request.POST)
            userinfo = form.save(commit=False)
            userinfo.user = user
            userinfo.save()
            message = f'成功新增！'    
        return render(request, 'userinfo.html', locals())
    else:
        message = "ERROR"
        print('出錯回首頁')
        redirect("/")

def logout(request):
    auth.logout(request)
    message = f'成功登出'
    return redirect('/')

def borrowBook(request, book_id):
    if request.user.is_active:
        book = Post.objects.get(id=book_id)
        if book!=book.isBorrow:
            due_date = timezone.now() + timezone.timedelta(days=90)
            borrowing_record = BorrowingRecord.objects.create(
                user=request.user, 
                book=book,
                borrowing_date=timezone.now(),
                is_returned=False, 
            )
            book.isBorrow=True
            book.save()
            return render(request, 'borrowBook.html', {'borrowing_record': borrowing_record,'msg':'借閱成功！'})
        else:
            return render(request, 'borrowBook.html', {'msg': '圖書暫不可借'})
    else:
        messages.warning(request, '尚未登入不可借書，請先登入')
        return redirect('login')
    
def returnBook(request):
    if request.method=='POST':
        u=None
        returnCorrect=[]
        returnBookList=request.POST.getlist('return_books')
        for recordingId in returnBookList:
            recording=BorrowingRecord.objects.get(id=recordingId)
            recording.is_returned=True
            recording.actual_return_date=timezone.now()
            returnCorrect.append(recording)
            recording.save()

            recording.book.isBorrow=False
            recording.book.save()
            u=recording.user
        return render(request, 'returnBook.html',{'returnCorrect':returnCorrect,
                                                  'u':u})
    else:
        return redirect('/')   
