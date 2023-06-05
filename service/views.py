from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'services/index.html')

def service_details(request, slug=None):
    return render(request, 'services/details.html')