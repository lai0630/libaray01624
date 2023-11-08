from django.db import models
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
