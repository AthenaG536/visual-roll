import datetime

from django.db import models
from django.forms import forms
from django.utils.datetime_safe import date, datetime
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


class User(models.Model):
    email = models.CharField('Email', max_length=320)
    first_name = models.CharField('First Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    password = models.CharField('password', max_length=255)
    def __str__(self):
        return '{} {}, email: {}'.format(self.first_name, self.last_name, self.email)


class Group(models.Model):
    g_name = models.CharField('Group Name', max_length=255)
    g_info = models.TextField('Group Info')
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField('Date Created', auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return '{} created by {}'.format(self.g_name, self.creator)

    class Meta:
        ordering = ['date_created']

class Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Date Joined', default=datetime.now, blank=True)
    def __str__(self):
        return '{} joined the {} group at: {}'.format(self.user, self.group, self.timestamp)

    class Meta:
        ordering = ['timestamp']

class Post(models.Model):
    details = models.TextField("Post Details")
    post_timestamp = models.DateTimeField('Date Joined', default=datetime.now, blank=True)
    def __str__(self):
        return self.details

    def was_published_recently(self):
        return self.post_timestamp >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        ordering = ['post_timestamp']

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
        return '{} {}, email:'.format(self.user, self.photo)

class Comment(models.Model):
    details = models.TextField('Comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_timestamp = models.DateTimeField('Date commented', default=datetime.now, blank=True)
    def __str__(self):
        return self.details

    class Meta:
        ordering = ['comment_timestamp']
