from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:

        if 'categories' in request.GET:
            category = request.GET['categories'].split(',')
            products = products.filter(categories__name__in=category)
            category = Category.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a keyword to search \
                    through the catalogue!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query) |
                       Q(categories__name__icontains=query))
            products = products.filter(queries)


    context = {
        'products': products,
        'search_term': query,
        'current_categories': category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a new painting to the store """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'The painting was added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add painting! Please ensure \
                that the form is valid!')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a painting """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'The painting was updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update painting! Please ensure \
                that the form is valid!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing painting "{product.title}"')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a painting """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to perform this task.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.info(request, 'The painting has been deleted!')
        return redirect('products')
    context = {'product': product}
    return render(request, 'products/delete_product.html', context)