from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductCategory, Brand
from django.urls import reverse
from django.db.models import Q
from .models import Review
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

# Create your views here.
def index(request, brand_slug=None, category_slug=None):
    products = Product.objects.filter(is_approved=True)
    category = None
    category_url = None

    query = request.GET.get('q')
    title = 'Your Ultimate Electronics Shop'
    if query:
        products = Product.objects.filter(is_approved=True, title__icontains=query) or Product.objects.filter(is_approved=True, description__icontains=query)
        title = f"{products.count()} Products matches query, '{query}'"
        category = 'Shops'
        category_url = reverse('shop:list')

    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = Product.objects.filter(category=category, is_approved=True)
        title = f"Products under Category, '{category}'"
        category = 'Categories'
        category_url = reverse('shop:list_by_category', kwargs={'category_slug': category_slug})

    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = Product.objects.filter(brand=brand, is_approved=True)
        title = f"Products under Brand, '{brand}'"
        category = 'Brands'
        category_url = reverse('shop:list_by_brand', kwargs={'brand_slug': brand_slug})

    if request.method == 'POST':
        price_range = request.POST.get('range')
        if price_range:
            min_price, max_price = price_range.split(' - ')
            
            products = Product.objects.filter(
                Q(current_price__gte=min_price) & Q(current_price__lte=max_price)
            )
    cart_product_form = CartAddProductForm()
    context = {
        'title': title,
        'brands': Brand.objects.all(),
        'product_categories': ProductCategory.objects.all(),
        'products': products,
        'category': category,
        'category_url': category_url,
        'popular_products': products[:3],
        'cart_product_form': cart_product_form
        
    }
    return render(request, 'shop/products/1.html', context)

def product_details(request, slug):
    product = get_object_or_404(Product, is_approved=True, slug=slug)
    blog_full_url = f"{request.scheme}://{request.get_host()}{product.get_absolute_url()}"
    related_products = Product.objects.filter(is_approved=True, category=product.category)
    cart_product_form = CartAddProductForm()
    context = {
        'title': product.title,
        'category': 'Our Shops',
        'category_url': reverse('shop:list'),
        'product': product,
        'product_full_url': blog_full_url,
        'product_text': f"Checkout this product, {product.title} on VSTech Limited Shop",
        'related_products': related_products,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/products/details.html', context)

@login_required
@require_POST
def leave_review(request, slug):
    product = get_object_or_404(Product, slug=slug, is_approved=True)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        message = request.POST.get('message')
        new_review = Review.objects.create(user=request.user, rating=rating, product=product, message=message)
        new_review.save()
        messages.success(request, 'Review added successfully.')
    return redirect('shop:detail', slug=slug)

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

    return redirect('shop:cart')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shop:cart')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'override': True})
    return render(request, 'shop/cart.html', {
        'cart': cart,
        'title': 'Shopping Cart',
        'category': 'Our Shop',
        'category_url': reverse('shop:list'),
    })

def checkout(request):
    return render(request, 'shop/checkout.html')