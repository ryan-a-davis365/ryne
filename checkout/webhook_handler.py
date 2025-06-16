from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from bag.contexts import bag_contents

import json
import time
import stripe
import sys
import traceback

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        try:
            cust_email = order.email
            subject = render_to_string(
                'checkout/confirmation_emails/confirmation_email_subject.txt',
                {'order': order})
            body = render_to_string(
                'checkout/confirmation_emails/confirmation_email_body.txt',
                {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )
            print("Confirmation email sent.")
        except Exception as e:
            print(f"Error sending confirmation email: {e}")
            traceback.print_exc(file=sys.stdout)

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        print(f"Unhandled webhook received: {event['type']}")
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

def handle_payment_intent_succeeded(self, event):
    print("Stripe webhook handler: handle_payment_intent_succeeded called")
    try:
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_country = shipping_details.address.country
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.default_town_or_city = shipping_details.address.city
                    profile.default_street_address1 = shipping_details.address.line1
                    profile.default_street_address2 = shipping_details.address.line2
                    profile.default_county = shipping_details.address.state
                    profile.save()
            except Exception as e:
                print(f"Error updating user profile: {e}")
                traceback.print_exc(file=sys.stdout)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
            except Exception as e:
                print(f"Error checking for existing order: {e}")
                traceback.print_exc(file=sys.stdout)
                break

        if order_exists:
            print("Order already exists, sending confirmation email.")
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                bag_dict = json.loads(bag)
                class FakeRequest:
                    pass
                fake_request = FakeRequest()
                fake_request.session = {'bag': bag_dict}
                bag_ctx = bag_contents(fake_request)
                order_total = bag_ctx['total']
                delivery_cost = bag_ctx['delivery']
                grand_total = bag_ctx['grand_total']

                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                    order_total=order_total,
                    delivery_cost=delivery_cost,
                    grand_total=grand_total,
                )
                for item_id, item_data in bag_dict.items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                print(f"Webhook error (order creation): {e}")
                traceback.print_exc(file=sys.stdout)
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        print("Order created, sending confirmation email.")
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)
    except Exception as e:
        print(f"Webhook error (outer): {e}")
        traceback.print_exc(file=sys.stdout)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | ERROR: {e}',
            status=500)

    def handle_payment_intent_payment_failed(self, event):
        print(f"Webhook received: {event['type']}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)