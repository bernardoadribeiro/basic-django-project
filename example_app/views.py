from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Successfully sent the email.')
        else:
            messages.error(request, 'Error while sending the email. Please try again later.')

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
