from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('topic')
            content = form.cleaned_data.get('message')
            send_to = ['claudiavomwalde@gmail.com']

            email = EmailMessage(
                subject,
                content,
                (send_to,),
            )
            email.send(fail_silently=False)
            messages.info(request, 'Tack för ditt meddelande!')
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Tack för ditt meddelande!')
#             return redirect('home')
#     else:
#         form = ContactForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'contact/contact.html', context)