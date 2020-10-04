import os

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from main.models import Post, Group, Members, User, Likedphoto, Likedpost, UserForm


class UserView(generic.DetailView):
    model = User
    fields = ["email", "first_name", "last_name", "password"]
    template_name = 'user.html'


class GroupView(generic.ListView):
    template_name = 'group.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        return Group.objects.order_by('-date_created')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'welcome.html')

def login_request(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                userbyemail = User.objects.get(email=email)
                user = User.authenticate(userbyemail, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {email}")
                    return redirect(user.get_absolute_url)
                else:
                    messages.error(request, "Invalid username or password.")
            except:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")
    form = UserForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

def register(request):
    return render(request, 'user.html')

def user_groups(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # members and group stuff
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

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:index")

class UserCreate(CreateView):
    model = User
    fields = ["email","first_name","last_name","password"]
    template_name = "register.html"
    success_url = "/login/"

class AuthorUpdate(UpdateView):
    model = User
    fields = ["email","first_name","last_name","password"]


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

