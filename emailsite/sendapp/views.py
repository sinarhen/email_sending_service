from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.

def index(request):
    return render(request, 'index.html')


def success(request):
    email = request.POST.get('email', '')
    data = """
    Hello there!

    I wanted to personally write an email in order to welcome you to our platform.\
     We have worked day and night to ensure that you get the best service. I hope \
    that you will continue to use our service. We send out a newsletter once a \
    week. Make sure that you read it. It is usually very informative.

    Cheers!"""
    send_mail('Subject', data, [email], fail_silently=False)
    return render(request, 'success.html')
