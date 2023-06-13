from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    """Contact form"""
    fullname = forms.CharField(label='Full name')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def send_email(self):
        fullname = self.cleaned_data['fullname'],
        email = self.cleaned_data['email'],
        subject = self.cleaned_data['subject'],
        message = self.cleaned_data['message']

        content = f'Nome: {fullname}\n E-mail:{email}\n Subject: {subject}\n Message: {message}'

        email = EmailMessage(
            subject='E-mail from Django Basic App',
            body=content,
            from_email='no-reply@django.test',
            to=['contact@django.test', ],
            headers={'Reply.To': email},
        )
        email.send()
