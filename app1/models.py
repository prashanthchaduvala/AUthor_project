from django.db import models

class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=10)
    is_verified=models.BooleanField(default=True)
    is_active = models.BooleanField(('active'), default=True)
    # is_author=models.BooleanField(default=False)

class News(models.Model):
    id=models.AutoField(primary_key=True)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    story=models.CharField(max_length=500)
    image=models.ImageField()
    date=models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.user_id)