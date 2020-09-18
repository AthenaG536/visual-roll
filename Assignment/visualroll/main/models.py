from django.db import models


class User(models.Model):
    email = models.TextField('Email')
    first_name = models.TextField('First Name')
    last_name = models.TextField('Last Name')
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    g_name = models.TextField('Group Name')
    g_info = models.TextField('Group Info')
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date_created = models.DateField('Date Created', auto_now_add=True)
    def __str__(self):
        return self.g_name


