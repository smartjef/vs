from django.shortcuts import render
from service.models import Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    return services