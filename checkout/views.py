from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RCKHWI04tFPjg9wj7Zyyj50df7FqetVYVVKmd15vurZdVTC63gnTXOn2o4Vg2QXxBIVIg2G8zJzrlrjW1x2879Q00rtDAJvhy',
    }

    return render(request, template, context)