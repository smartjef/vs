from django.shortcuts import render
from .models import Service
# Create your views here.
def index(request):
    context = {
        'title': 'Our Services',
        'services': Service.objects.all(),
    }
    return render(request, 'services/index.html', context)

def service_details(request, slug=None):
    return render(request, 'services/details.html')