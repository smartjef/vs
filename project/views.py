from django.shortcuts import render
from .models import Project
# Create your views here.
def index(request):
    context = {
        'title': 'Projects',
        'projects': Project.objects.filter(is_active=True),
    }
    return render(request, 'projects/index.html', context)

def service_details(request, slug):
    return render(request, 'projects/details.html')