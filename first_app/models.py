from django.db import models
from django.contrib.auth.models import User
class SAVE(models.Model):
    name=models.CharField(max_length=264)
    email=models.EmailField(max_length=254,unique=True)
    vemail=models.EmailField(max_length=254,unique=True)
    text=models.CharField(max_length=10000)
    # def __str__(self):
    #     return "%s %s %s %s" % (self.name, self.email, self.vemail,
    #     self.text)
# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.DO_NOTHING)
    date=models.DateField()
    def __str__(self):
        return str(self.date)
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
# class Movie_list(models.Model):
#     movieid = models.CharField(max_length=6)
#     name = models.CharField(max_length=100)
#     date=  models.CharField(max_length=50)
#     address = models.CharField(max_length=100, blank=True)
