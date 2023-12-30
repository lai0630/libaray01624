from django.contrib import admin
from mysite.models import Post,Mood,Commet
from django.contrib import admin
from mysite import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class CommetAdmin(admin.ModelAdmin):
    list_display=('nickname', 'message', 'enabled', 'pub_time')
    ordering=('-pub_time',)
admin.site.register(models.Mood)
admin.site.register(models.Commet, CommetAdmin)
admin.site.register(Post, PostAdmin)