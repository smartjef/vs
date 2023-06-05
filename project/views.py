from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'projects/index.html')

def service_details(request, slug):
    return render(request, 'projects/details.html')