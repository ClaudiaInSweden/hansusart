from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Inquiry
from .forms import InquiryForm
from products.models import Product
from django.contrib import messages


def inquiry(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.POST.get('redirect_url')
    if request.method == 'POST':
        form = InquiryForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Tack för ditt meddelande!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Formuläret kunde inte sändes. Vänligen kontrollera att allt är ifyllt korrekt.')
            form = InquiryForm(instance=product)
    else:
        form = InquiryForm(instance=product)

    template = 'inquiry/inquiry.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)