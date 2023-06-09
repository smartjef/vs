from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from random import randint
from service.models import Service
from project.models import Project
from blog.models import Post
from .models import Testimony, Partner, FAQ, Contact
# Create your views here.
def index(request):
    random_number = randint(1,10)
    context = {
        'title' : 'Homepage',
        'services': Service.objects.all(),
        'projects': Project.objects.filter(is_active=True),
        'testimonies': Testimony.objects.filter(is_active=True)[:6],
        'partners': Partner.objects.all(),
        'faqs': FAQ.objects.filter(is_active=True)[:5],
        'blogs': Post.objects.filter(is_published=True)[:3],
    }
    return render(request, f'index/1.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        email = request.POST.get('user_email')
        subject = request.POST.get('subject')
        if subject:
            subject = subject
        else:
            subject = 'Contact by ' + name + ' - ' + email + ' - ' + 'No Subject'
        message = request.POST.get('message')
        phone_number = request.POST.get('phone')
        contact = Contact(name=name, email=email, subject=subject, message=message, phone_number=phone_number)
        contact.save()
        messages.success(request, 'Contact request submitted successfully.')
        # send_mail(subject,message, email, ['o.jeff3.a@gmail.com','lawiomosh3@gmail.com'],fail_silently=False,)
        return redirect('index')

    context = {
        'title': 'Contact Us'
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        'title': 'About Us',
        'partners': Partner.objects.all(),
        'projects': Project.objects.filter(is_active=True),
    }
    return render(request, 'about.html', context)

def testimonies(request):
    context = {
        'title': 'Testimonies',
        'testimonies': Testimony.objects.filter(is_active=True),
    }
    return render(request, 'testimonial.html', context)

def faq(request):
    context = {
        'title': 'FAQs',
        'faqs': FAQ.objects.filter(is_active=True),
    }
    return render(request, 'faq.html', context)