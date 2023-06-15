from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory, Brand
from django.urls import reverse
from django.db.models import Q
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

    context = {
        'title': title,
        'brands': Brand.objects.all(),
        'product_categories': ProductCategory.objects.all(),
        'products': products,
        'category': category,
        'category_url': category_url,
        'popular_products': products[:3]
        
    }
    return render(request, 'shop/products/1.html', context)

def product_details(request, slug):
    return render(request, 'shop/products/details.html')

def cart(request):
    return render(request, 'shop/cart.html')

def checkout(request):
    return render(request, 'shop/checkout.html')