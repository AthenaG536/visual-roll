import datetime

import django
from django.db import models
from django.forms import ModelForm, forms
from django.urls import reverse
from django.utils.datetime_safe import date, datetime
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# Classes
class User(models.Model):
    email = models.CharField('Email', max_length=320, unique=True)
    first_name = models.CharField('First Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    password = models.CharField('password', max_length=255)
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_user_email(self):
        return '{} {}, email: {}'.format(self.first_name, self.last_name, self.email)

    def get_absolute_url(self):
        return reverse('account/%s/' % self.id)

    def check_password(self,entered_password):
        if self.password == entered_password:
            return True
        else:
            return False
    def get_related_members(self):
        member_list = Members.objects.filter(User=self)
        return member_list

    def authenticate(self, password=None):
        try:
            #  Check the password is the reverse of the username
            if self.check_password(self, password):
                # Yes? return the Django user object
                return self
            else:
                # No? return None - triggers default login failed
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

class Group(models.Model):
    g_name = models.CharField('Group Name', max_length=255)
    g_info = models.TextField('Group Info')
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField('Date Created', auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return '{}'.format(self.g_name)
    def get_group_by_creater(self):
        return '{} created by {}'.format(self.g_name, self.creator)
    def get_absolute_url(self):
        return reverse('/%s/mygroups' % self.id)
    def get_related_members(self):
        member_list = Members.objects.filter(Group=self)
        return member_list

    class Meta:
        ordering = ['date_created']

class Members(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Date Joined', default=datetime.now, blank=True)
    def __str__(self):
        return '{} joined the {} group at: {}'.format(self.user, self.group, self.timestamp)
    def get_absolute_url(self):
        return '/%s/' % self.name

    class Meta:
        ordering = ['timestamp']





class Post(models.Model):
    details = models.TextField("Post Details")
    post_timestamp = models.DateTimeField('Posted Date', default=datetime.now, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=id(Group))
    def __str__(self):
        return self.details

    def was_published_recently(self):
        return self.post_timestamp >= timezone.now() - datetime.timedelta(days=1)
    def get_absolute_url(self):
        return '/%s/' % self.name

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    class Meta:
        ordering = ['post_timestamp']

class Likedpost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return '/%s/' % self.name

class Photo(models.Model):
    image = models.ImageField(upload_to="photos")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
    def get_absolute_url(self):
        return '/%s/' % self.name

class Likedphoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}, email:'.format(self.user, self.photo)
    def get_absolute_url(self):
        return '/%s/' % self.name

class Comment(models.Model):
    details = models.TextField('Comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_timestamp = models.DateTimeField('Date commented', default=datetime.now, blank=True)
    def __str__(self):
        return self.details
    def get_absolute_url(self):
        return '/%s/' % self.name

    class Meta:
        ordering = ['comment_timestamp']


# Forms
class UserForm(ModelForm):
    password = django.forms.CharField(widget=django.forms.PasswordInput())
    class Meta():
        model = User
        fields = ('email', 'password')


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["g_name", "g_info"]

