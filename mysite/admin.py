from django.contrib import admin
from mysite.models import Post,Mood,Comment
from django.contrib import admin
from mysite import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class CommentAdmin(admin.ModelAdmin):
    list_display=('mood','nickname', 'message', 'enabled', 'pub_time')
    ordering=('-pub_time',)
admin.site.register(models.Mood)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)