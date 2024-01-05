from django.contrib import admin
from mysite.models import Post,Mood,Comment,BorrowingRecord
from django.contrib import admin
from mysite import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class CommentAdmin(admin.ModelAdmin):
    list_display=('mood','nickname', 'message', 'enabled', 'pub_time')
    ordering=('-pub_time',)

class ProfileAdmin(admin.ModelAdmin):
    list_display=('preferences','gender','favorite')

class BorrowingRecordAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'borrowing_date', 'actual_return_date', 'is_returned']
admin.site.register(models.Mood)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(models.Preferences)
admin.site.register(models.Profile,ProfileAdmin)
admin.site.register(BorrowingRecord, BorrowingRecordAdmin)