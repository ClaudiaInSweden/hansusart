from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Category
from .forms import BlogForm

# Create your views here.
class BlogView(ListView):
    model = Blog
    queryset = Blog.objects.filter(status='Published')
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'



def add_blogpost(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'The blog post has been added successfully!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blogpost! Please make sure \
                that the form is valid!')
    else:
        form = BlogForm()
    template = 'blog/add_blogpost.html'
    context = {'form': form,}

    return render(request, template, context)