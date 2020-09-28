from django.db import models
from django.forms import forms
from django.utils.datetime_safe import date, datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class User(models.Model):
    email = models.CharField('Email', max_length=320)
    first_name = models.CharField('First Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    password = models.CharField('password', max_length=255)
    def __str__(self):
        return self.email


class Group(models.Model):
    g_name = models.CharField('Group Name', max_length=255)
    g_info = models.TextField('Group Info')
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField('Date Created', auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.g_name

    class Meta:
        ordering = ['date_created']

class Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Date Joined', default=datetime.now, blank=True)
    def __str__(self):
        str = ""
        str = str + User.get(self.user).first_name + " joined the " + Group.get(self.group).g_name + " group at: " + self.timestamp
        return str

    class Meta:
        ordering = ['timestamp']

class Post(models.Model):
    details = models.TextField("Post Details")
    def __str__(self):
        return self.details

class Likedpost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Photo(models.Model):
    image = models.ImageField(upload_to="photos")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

class Likedphoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        str = ""
        str = str + User.get(self.user).first_name + " liked " + Photo.get(self.photo).image.name
        return str

class Comment(models.Model):
    details = models.TextField('Comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenttimestamp = models.DateTimeField('Date commented', default=datetime.now, blank=True)
    def __str__(self):
        return self.details

    class Meta:
        ordering = ['commenttimestamp']
