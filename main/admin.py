from django.contrib import admin

from .models import User, Group, Members, Post, Photo, Likedpost, Likedphoto, Comment

# Registering models
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Members)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Likedpost)
admin.site.register(Likedphoto)
admin.site.register(Comment)