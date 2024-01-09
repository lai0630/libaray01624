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

class UserRegisterForm(forms.Form):
    user_name = forms.CharField(label='您的帳號', max_length=50)
    user_email = forms.EmailField(label='電子郵件')
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput )
    user_password_confirm = forms.CharField(label='輸入確認密碼', widget=forms.PasswordInput)

class LoginForm(forms.Form):
    user_name = forms.CharField(label='您的帳號', max_length=50)
    user_password = forms.CharField(label='輸入密碼', widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile#跟哪個資料庫相關
        fields = ['preferences', 'gender', 'favorite']#定義要儲存欄位(要跟上面的一樣就是要跟Post有關聯)
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['preferences'].label = '偏好哪種小說'#有引用到model的mood
        self.fields['gender'].label = '性別'#預設值在model
        self.fields['favorite'].label = '最喜歡哪本書'