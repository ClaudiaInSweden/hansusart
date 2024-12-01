from django.shortcuts import render, redirect
from blog.models import Blog, Category

# Create your views here.
def index(request):

    posts = Blog.objects.filter(highlight='True')

    context= {
        'posts': posts,
    }

    return render(request, 'home/index.html', context)


def about(request):

    return render(request, 'home/about.html')


def terms(request):

    return render(request, 'home/villkor.html')