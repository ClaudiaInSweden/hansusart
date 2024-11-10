from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Inquiry
from .forms import InquiryForm
from products.models import Product
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string


def inquiry(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    redirect_url = request.POST.get('redirect_url')
    if request.method == 'POST':
        form = InquiryForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            street1 = form.cleaned_data.get('street1')
            street2 = form.cleaned_data.get('street2')
            postcode = form.cleaned_data.get('postcode')
            city = form.cleaned_data.get('city')
            message = form.cleaned_data.get('message')
            painting = request.POST.get('product')
            send_to = ['claudiavomwalde@gmail.com',]

            html = render_to_string('inquiry/emails/inquiryform.html', {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone_number': phone_number,
                'street1': street1,
                'street2': street2,
                'postcode': postcode,
                'city': city,
                'message': message,
                'painting': painting,
            })

            send_mail('HannelesArt Köpförfrågan', 'Meddelande', 'claudiavomwalde@gmail.com', ['claudiavomwalde@gmail.com'], html_message=html) 


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