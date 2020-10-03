from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from main.models import Post, Group, Members, User, Likedphoto, Likedpost


def index(request):
    return render(request, 'index.html')

def register(request):
    return HttpResponse("Welcome to Visual Roll.")

def user_groups(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # members and group stuff
    return render(request, 'user.html', {'user': user})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user.html', {'user': user})

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'group.html', {'group': group})

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

#
# def user_login(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = loginForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})
#     return HttpResponse("Welcome to Visual Roll.")

