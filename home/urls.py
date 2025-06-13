from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_us, name='contact_us'),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
    path('contact/confirmation/', views.contact_confirmation, name='contact_confirmation'),
    path('newsletter-signup/confirmation/', views.newsletter_confirmation, name='newsletter_confirmation'),
]
