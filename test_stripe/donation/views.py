from django.shortcuts import render
import stripe
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from .models import item

#Payment success

def payment_success(request):
    
    return render(request, 'donation/payment-success.html')


#Payment failed


def payment_failed(request):
    
    return render(request, 'donation/payment-failed.html')



def product(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    
    session = stripe.checkout.Session.create(
    line_items=[{
      
      'price': 'price_1M9F51A86dmAOzEvMSHKRBKC',
      
      'quantity': 1,
    }],
    
    mode='payment',
    success_url = request.build_absolute_uri(reverse('payment-success')) + '?session_id = {CHECKOUT_SESSION_ID}',
    
    cancel_url  = request.build_absolute_uri(reverse('payment-failed'))
    )
    
    item_info = item.objects.all()
    context = {'session_id': session.id, 'stripe_public_key': settings.STRIPE_PUBLIC_KEY, 'item_name': item_info[0].name, 'item_description': item_info[0].description, 'item_price': item_info[0].price}
    
    return render(request, 'donation/item.html', context=context)

