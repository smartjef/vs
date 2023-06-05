from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shop/products/1.html')

def product_details(request, slug=None):
    return render(request, 'shop/products/details.html')

def cart(request):
    return render(request, 'shop/cart.html')

def checkout(request):
    return render(request, 'shop/checkout.html')