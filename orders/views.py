from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from shop.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required

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
            # launch asynchronous task
            order_created.delay(order.id)
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

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'shop/orders/order/detail.html', {'order': order})