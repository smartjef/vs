from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def blog_detail(request, slug=None):
    return render(request, 'blog/details.html')