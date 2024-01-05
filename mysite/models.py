from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    isBorrow = models.BooleanField(("外借中"),default=False)
    
    @property
    def formatted_is_borrow(self):
        if self.isBorrow:
            return '<span style="color:white;background-color:red;border: 1px soild white; padding: 3px; border-radius: 3px;">外借中</span>'
        else:
            return '<span style="color:white;background-color:green;border: 1px soild white; padding: 3px; border-radius: 3px;">可借閱</span>'
    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.status

class Comment(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    message = models.TextField(null=False)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)
    
    def __str__(self):
        return self.message

class Preferences(models.Model):
    status = models.CharField(max_length=10, null=False)
    def __str__(self):
        return self.status
    
class Profile(models.Model):
    Gender = (
        ('M', '男性'),#前面是真正儲存的內容 後面是顯示的
        ('W', '女性'),
    )
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)#一對一的欄位 指到的欄位是auth.models.User(內建的)
    preferences = models.ForeignKey('Preferences', on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=Gender)
    favorite = models.CharField(max_length=10)
	
    def __str__(self):
        return self.user.username   

class BorrowingRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Post, on_delete=models.CASCADE)
    borrowing_date = models.DateField(auto_now_add=True)
    actual_return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} 借閱 {self.book}"
    