from django.db import models
from django.contrib.auth.models import User


class ContactSubmission(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.email}) - {self.submitted_at:%Y-%m-%d %H:%M}"


class NewsletterSignup(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    agreed = models.BooleanField(default=False)
    signed_up_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.email}) - {self.signed_up_at:%Y-%m-%d %H:%M}"