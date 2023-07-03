from django.shortcuts import render

# Create your views here.
def chat(request):
    return render(request, 'ai/chat.html')

def desc_to_image(request):
    return render(request, 'ai/desc_to_image.html')