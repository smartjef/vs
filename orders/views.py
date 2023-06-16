from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from shop.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['current_price'], quantity=item['quantity'])
                # clear the cart
            cart.clear()
            messages.success(request, 'Thank You, Order Created Successfully, if payment is made via M-Pesa, please keep the message or Code!')
            return redirect('shop:list')
    else:
        form = OrderCreateForm()
    
    context = {
        'title': 'Create Order',
        'category': 'Our Shop',
        'category_url': reverse('shop:list'),
        'cart': cart, 
        'form': form
    }

    return render(request,'shop/orders/order/create.html', context)