from django.contrib import admin
from .models import ContactSubmission, NewsletterSignup


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'submitted_at')
    search_fields = ('username', 'email', 'message')
    readonly_fields = ('username', 'email', 'message', 'submitted_at', 'user')


@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'agreed', 'signed_up_at')
    search_fields = ('username', 'email')
    readonly_fields = ('username', 'email', 'agreed', 'signed_up_at', 'user')