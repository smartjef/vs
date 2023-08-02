from datetime import datetime
from .models import About
from users.models import Team
from shop.cart import Cart
from assignments.models import AreaChoice, LevelChoice, Period, ProjectPeriod

def all(request):
    current_year = datetime.now().year
    return {
        'current_year': current_year,
        'about': About.objects.filter(is_active=True).first(),
        'teams': Team.objects.filter(is_active=True),
        'cart': Cart(request),
        'subject_area': AreaChoice.objects.all(),
        'academic_level':LevelChoice.objects.all(),
        'period': Period.objects.filter(is_active=True),
        'project_period': ProjectPeriod.objects.all()
    }
