from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


# Create your views here.

def index(request):
    form = ContactForm()
    print('INDEX')
    if request.method == 'POST':
        print('POST')
        form = ContactForm(request.POST)
        if form.is_valid():
            print('VALID')
            email = form.cleaned_data['email']
            data = """
            Hello there!
        
            I wanted to personally write an email in order to welcome you to our platform.\
             We have worked day and night to ensure that you get the best service. I hope \
            that you will continue to use our service. We send out a newsletter once a \
            week. Make sure that you read it. It is usually very informative.
        
            Cheers!"""
            send_mail('Subject', data, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[email],
                      fail_silently=False)
            print('SENDED')
            print(email)
            return redirect('success')
    context = {'form': form}
    return render(request, 'sendapp/index.html', context=context)


def success(request):
    return render(request, 'sendapp/success.html')
