from django.db import models

class User(models.Model):
    email = models.TextField('Email')
    first_name = models.TextField('First Name')
    last_name = models.TextField('Last Name')
    password = models.TextField('Password')

