from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    schools = School.objects.filter(is_active=True)
    unit_names = UnitName.objects.filter(is_active=True)
    notes = Note.objects.filter(is_active=True)

    context = {
        'notes': notes,
        'schools': schools,
        'units': unit_names
    }

    return render(request, 'edu/index.html', context)

def resources(request):
    schools = School.objects.filter(is_active=True)
    unit_names = UnitName.objects.filter(is_active=True)
    notes = Note.objects.filter(is_active=True)

    context = {
        'notes': notes,
        'schools': schools,
        'units': unit_names
    }

    return render(request, 'edu/index.html', context)