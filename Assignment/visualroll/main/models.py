from django.db import models
from django.forms import forms
from django.utils.datetime_safe import date, datetime


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
    date_created = models.DateField('Date Created', default=date.today, blank=True)

    def __str__(self):
        return self.g_name

class GroupUser(models.Model):
    user = models.ForeignObject(User, on_delete=models.CASCADE)
    Group = models.ForeignObject(Group, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Date Joined', default=datetime.now, blank=True)
