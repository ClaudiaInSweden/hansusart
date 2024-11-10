from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('topic')
            content = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            send_to = ['claudiavomwalde@gmail.com',]

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'content': content
            })

            send_mail('HannelesArt Kontaktformulär', 'Meddelande', 'claudiavomwalde@gmail.com', ['claudiavomwalde@gmail.com'], html_message=html) 
            messages.info(request, 'Tack för ditt meddelande!')
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
