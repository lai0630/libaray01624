from django.contrib import admin
from mysite.models import Post,Mood,Commet

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class CommetAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','pub_date')#可以看product跟這兩個的差別

admin.site.register(Post, PostAdmin)
admin.site.register(Mood)
admin.site.register(Commet,CommetAdmin)