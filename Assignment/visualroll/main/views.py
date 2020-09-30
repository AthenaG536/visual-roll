from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from main.models import Post


def index(request):
    return render(request, 'index.html')

def register(request):
    return HttpResponse("Welcome to Visual Roll.")

def create_group(request):
    return HttpResponse("Welcome to Visual Roll.")

def view_group(request, group_id):
    return HttpResponse("Group name: %s" % group_id)

def group_posts(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    output = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(output, request))

def view_photo(request, photo_id):
    return HttpResponse("Photo name: %s" % photo_id)

def members(request, member_id):
    return HttpResponse("Member: %s" % member_id)