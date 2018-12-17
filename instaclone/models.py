from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q


# Create your models here.
Gender=(
    ('Male','Male'),
    ('Female','Female'),
)

class Location(models.Model):
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='photos/')
    fullname = models.CharField(max_length=255)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = HTMLField()
    email = models.EmailField()
    phonenumber = models.IntegerField()
    gender = models.CharField(max_length=15,choices=Gender,default="Male")

    def __str__(self):
        return self.username.username

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(username__username=search_term) | Q(fullname__icontains=search_term))
        return profiles

class Post(models.Model):
    photo_pic = models.ImageField(upload_to = 'photos/')
    caption = models.CharField(max_length=3000)
    upload_by = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    def save_photo(self, user):
        self.save()

    @classmethod
    def all_photos(cls):
        all_photos = cls.objects.all()
        return all_photos

    @classmethod
    def user_photos(cls, username):
        photos = cls.objects.filter(uploaded_by__username=username)
        return photos

    @classmethod
    def filter_by_caption(cls, search_term):
        return cls.objects.filter(caption__icontains=search_term)

    def save_photo(self, user):
        self.save()


class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()


# class Follower(models.Model):
#     username = models.ForeignKey(User)
#     followers = models.ForeignKey(User)
#
# class Following(models.Model):
#     username = models.ForeignKey(User)
#     followings = models.ForeignKey(User)
