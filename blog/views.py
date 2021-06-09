from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Blog
from.forms import CreateBlogForm, SignUpForm, LoginForm

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home.html', context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateBlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CreateBlogForm()
        context = {
            'form': form
        }
        return render(request, 'blog/create.html', context)
    else:
        return HttpResponseRedirect('/login/')


def update(request, blog_id):
    if request.user.is_authenticated:
        blogs = Blog.objects.get(pk=blog_id)

        if request.method == 'POST':
            form = CreateBlogForm(request.POST, request.FILES, instance=blogs)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = CreateBlogForm(instance=blogs)

        context = {
            'form': form
        }
        return render(request, 'blog/update.html', context)
    else:
        return HttpResponseRedirect('/login/')

def delete(request, blog_id):
    if request.user.is_authenticated:
        blogs = Blog.objects.get(pk=blog_id)
        blogs.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'blog/signup.html', context)

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = LoginForm()
        context = {'form': form}
        return render(request, 'blog/login.html', context)
    else:
        return redirect('home')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



