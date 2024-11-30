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
            post = form.save()
            messages.success(request, 'The blog post has been added successfully!')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add blogpost! Please make sure \
                that the form is valid!')
    else:
        form = BlogForm()
    template = 'add_blogpost.html'
    context = {'form': form,}

    return render(request, template, context)



@login_required
def edit_blogpost(request, post_id):
    """ Edit a blogpost """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    post = get_object_or_404(Blog, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Bloginlägget har uppdaterats!')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update blogpost! Please ensure \
                that the form is valid!')
    else:
        form = BlogForm(instance=post)
        
    template = 'edit_blogpost.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_blogpost(request, post_id):
    """ Delete a painting """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    post = get_object_or_404(Blog, pk=post_id)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'The blogpost has been deleted!')
        return redirect('blog')
    context = {'post': post}
    return render(request, 'delete_blogpost.html', context)