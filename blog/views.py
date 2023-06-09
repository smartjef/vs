from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    context = {
        'title':'Blogs',
        'blogs': Post.objects.filter(is_published=True),
    }
    return render(request, 'blog/index.html', context)

def blog_detail(request, slug=None):
    return render(request, 'blog/details.html')