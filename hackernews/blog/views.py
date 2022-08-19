import re
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserChangeForm , UserCreationForm , PasswordChangeForm
from django.contrib.auth.models import  User
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post
# Create your views here.
def login_custom(request):
    if request.user.is_authenticated:
        return redirect('admin:index')
    form = 'login'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , 'user dose not exists go to register page')
            return redirect('login')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('admin:index')

    return render(request , 'login.html' , context={"form":form})

def logout_custom(request):
    logout(request)
    return redirect('login')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if user is not None:
                login(request , user)
                return redirect('admin:index')
    return render(request , 'register.html' , context={"form":form})

def userchangepassword(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST , user=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request , 'changepassword.html' , context={"form" : form})

def post_all(request):
    posts = Post.objects.all()
    paginator = Paginator(posts , 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request , 'posts.html' , context={"page_obj":page_obj})

def post(request , slug):
    post = Post.objects.get(slug=slug)
    return render(request , 'post.html' , context={"post":post})