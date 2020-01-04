# Code taken from Code Institute Ecommerce app project

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe
from django.http import request


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    discount = 20
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()            
            cart = request.session.get('cart', {}) 
            sub_total = 0          
            total = 0           
         
          
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id) 
                sub_total += quantity * product.price
                total += quantity * product.price        
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                if total >= 80:
                    total = total - discount
                else:
                    total = total                                     
                             
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid and your products are on there way")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
       if request.method == "GET":
           
        payment_form = MakePaymentForm(request.GET)
        order_form = OrderForm(request.GET)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()            
            cart = request.session.get('cart', {}) 
            sub_total = 0          
            total = 0           
         
          
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id) 
                sub_total += quantity * product.price
                total += quantity * product.price        
                order_line_item = OrderLineItem(
                    order = order, 
                    product = product, 
                    quantity = quantity
                    )
                order_line_item.save()
                if total >= 80:
                    total = total - discount
                else:
                    total = total     
        
    return render(request, "checkout/checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})