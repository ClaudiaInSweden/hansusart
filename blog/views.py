from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog, Category
from .forms import BlogForm

# Create your views here.
class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'


# def blog(request):

#     blog = Blog.objects.all()
   
#     context = {
#         'blog': blog,
#     }

#     return render(request, 'blog.html', context)


# def blog_detail(request, blog_id):

#     blogpost = get_object_or_404(Blog, pk=blog_id)

#     context = {
#         'blogpost': blogpost,
#     }

#     return render(request, 'blog_detail.html', context)


# def category_list(request, cats):

#     blog_category = Blog.objects.filter(categories=cats)

#     context = {
#         'cats': cats,
#         'blog_category': blog_category,
#     }

#     return render(request, 'categories.html', context)


def add_blogpost(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blogpost = form.save()
            messages.success(request, 'The blog post has been added successfully!')
            return redirect(reverse('blog_detail', args=[blogpost.id]))
        else:
            messages.error(request, 'Failed to add blogpost! Please make sure \
                that the form is valid!')
    else:
        form = BlogForm()
    template = 'blog/add_blogpost.html'
    context = {'form': form,}

    return render(request, template, context)