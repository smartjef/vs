from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Get Work Done',
    }
    return render(request, 'assignments/index.html', context)

# Create your views here.
def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'assignments/dashboard.html', context)