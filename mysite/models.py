from django.db import models
from datetime import datetime
from django.utils import timezone

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

class Commet(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message

    

