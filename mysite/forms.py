from django import forms#表單推薦用這種寫法 ppt50幾頁
from mysite import models
from mysite.models import Comment


class CommentForm(forms.ModelForm):#表單會連到資料庫
    class Meta:#跟哪個資料庫相關
        model = Comment#會連到資料庫的Post裡面
        fields = ['mood', 'nickname', 'message']#定義要儲存欄位(要跟上面的一樣就是要跟Post有關聯)
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'#有引用到model的mood
        self.fields['nickname'].label = '你的暱稱'#預設值在model
        self.fields['message'].label = '心情留言'