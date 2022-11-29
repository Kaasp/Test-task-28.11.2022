from django.urls import path
from . import views
#from views import CreateCheckoutSessionView

urlpatterns = [
    
    #Payment success
    
    path('payment-success', views.payment_success, name = 'payment-success'),
    
    #Payment failed

    path('payment-failed', views.payment_failed, name = 'payment-failed'),
    
    
    path('item/1', views.product, name = 'item'),
    
]