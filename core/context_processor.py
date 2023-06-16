from datetime import datetime
from .models import About
from users.models import Team
from shop.cart import Cart

def all(request):
    current_year = datetime.now().year
    return {
        'current_year': current_year,
        'about': About.objects.filter(is_active=True).first(),
        'teams': Team.objects.filter(is_active=True),
        'cart': Cart(request),
    }
