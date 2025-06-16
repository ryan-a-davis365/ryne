from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
import sys
import traceback

@require_POST
@csrf_exempt
def webhook(request):
    print("Stripe webhook endpoint called")
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # get the webhook data and verify its signature
    payload = request.body
    print("Payload received")
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    print(f"Signature header: {sig_header}")
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
        print("Stripe event constructed")
    except ValueError as e:
        print(f"ValueError: {e}")
        traceback.print_exc(file=sys.stdout)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(f"SignatureVerificationError: {e}")
        traceback.print_exc(file=sys.stdout)
        return HttpResponse(status=400)
    except Exception as e:
        print(f"Other Exception: {e}")
        traceback.print_exc(file=sys.stdout)
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type from Stripe
    event_type = event['type']
    print(f"Event type: {event_type}")

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    try:
        response = event_handler(event)
        print("Handler executed")
        return response
    except Exception as e:
        print(f"Error in event handler: {e}")
        traceback.print_exc(file=sys.stdout)
        return HttpResponse(content=f"Error in event handler: {e}", status=500)