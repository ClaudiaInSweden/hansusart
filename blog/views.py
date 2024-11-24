from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Blog, Category

# Create your views here.
def blog(request):

    blog = Blog.objects.all()
   
    context = {
        'blog': blog,
    }

    return render(request, 'blog.html', context)


def blog_detail(request, blog_id):

    blogpost = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'blog_detail.html', context)