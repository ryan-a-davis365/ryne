from django.shortcuts import render, redirect
from .models import ContactSubmission, NewsletterSignup
from django.core.mail import send_mail


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def contact_us(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')
        user = request.user if request.user.is_authenticated else None

        ContactSubmission.objects.create(
            user=user,
            username=username,
            email=email,
            message=message
        )

        body = f"Username: {username}\nEmail: {email}\n\nMessage:\n{message}"
        send_mail(
            subject='New Contact Form Submission',
            message=body,
            from_email=None,
            recipient_list=['projectryne@gmail.com'],
            fail_silently=False,
        )
        return redirect('contact_confirmation')
    return render(request, 'contact_us.html')

def contact_confirmation(request):
    return render(request, 'contact_confirmation.html')

def newsletter_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        agreed = request.POST.get('agree') == 'on'
        user = request.user if request.user.is_authenticated else None
        NewsletterSignup.objects.create(
            user=user,
            username=username,
            email=email,
            agreed=agreed
        )
        send_mail(
            subject='Welcome to the RYNE Newsletter!',
            message=f'Hi {username},\n\nThank you for signing up for the RYNE newsletter. Stay tuned for updates and exclusive offers!',
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )
        return redirect('newsletter_confirmation')
    return render(request, 'newsletter_signup.html')

def newsletter_confirmation(request):
    return render(request, 'newsletter_confirmation.html')