from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscriber, MailMessage
from main.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.db import IntegrityError
from django.views.decorators.http import require_POST
from shop.models import Product
from blog.models import Post
from core.models import Testimony
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from functools import wraps
# Create your views here.

def user_must_be_staff(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to the index page or any other desired URL
            return redirect('index')
    return wrapper

@require_POST
def new_subscriber(request):

    if request.method == 'POST':
        name = ''
        email = request.POST.get('email')
        if request.user.is_authenticated and request.user.get_full_name():
            name = request.user.get_full_name()
    try:
        subscriber = Subscriber.objects.create(name=name, email=email)
        subscriber.save()
        messages.info(request, "Successfull subscription")
    except IntegrityError:
        messages.warning(request, "Already Subscribed")

    return redirect('index')

@login_required
@user_must_be_staff
def index(request):
    context = {
        'title': 'Subscribers Page',
        'subscribers': Subscriber.objects.all(),
    }
    return render(request, 'newsletter/index.html', context)

@login_required
@user_must_be_staff
def product(request):
    products = Product.objects.all()
    column_2 = products[:int(len(products)/2)]
    column_3 = products[int(len(products)/2):]
    column_1_1 = column_2[int(len(column_2)/2)]
    column_1_2 = column_3[int(len(column_3)/2)]

    context = {
        'title': 'Products HTML Template',
        'column_2': column_2,
        'column_3': column_3,
        'column_1_1': column_1_1,
        'column_1_2': column_1_2,
    }
    return render(request, 'newsletter/templates/products.html', context)

@login_required
@user_must_be_staff
def view_templates(request):
    context = {
        'title': 'HTML Email Template',
    }
    return render(request, 'newsletter/templates/index.html', context)

@login_required
def unsubscribe(request, email):
    subscriber = get_object_or_404(Subscriber, email=email, is_subscribed=True)
    subscriber.is_subscribed = False
    subscriber.save()
    messages.info(request, "Unsubscribed successfully")
    return redirect('index')

@login_required
@user_must_be_staff
def blogs(request):
    context = {
        'title': 'Blogs HTML Template',
        'blogs': Post.objects.filter(is_published=True)[:4],
        'testimonies': Testimony.objects.filter(is_active=True)[:2]
    }
    return render(request, 'newsletter/templates/blogs.html', context)

@login_required
@user_must_be_staff
def default(request):
    context = {
        'title': 'Default HTML Template'
    }
    return render(request, 'newsletter/templates/default.html', context)

@login_required
@user_must_be_staff
def send_email_to_subscribers(request):
    context = {}
    if request.method == 'POST':
        subject = request.POST.get('subject')
        template = request.POST.get('template')
        message = request.POST.get('message')

        if template == 'default':
            if not message:
                messages.warning(request, "Default Theme can be sent with blank Message")
                return redirect('subscribe:send_email')
            else:
                context = {
                    'title': subject,
                    'content': message,
                    'author': request.user,
                    'recipient_email': '',
                    'recipient_name': '',
                }

        if template == 'blogs':
            context = {
                'title': subject,
                'blogs': Post.objects.filter(is_published=True)[:2],
                'testimonies': Testimony.objects.filter(is_active=True)[:2]
            }

        if template == 'products':
            products = Product.objects.all()
            column_2 = products[:int(len(products)/2)]
            column_3 = products[int(len(products)/2):]
            column_1_1 = column_2[int(len(column_2)/2)]
            column_1_2 = column_3[int(len(column_3)/2)]

            context = {
                'title': subject,
                'column_2': column_2,
                'column_3': column_3,
                'column_1_1': column_1_1,
                'column_1_2': column_1_2,
            }

        subscribers = Subscriber.objects.filter(is_subscribed=True)
        if subscribers:
            mail_message = MailMessage.objects.create(
                subject=subject,
                message=message,
                author=request.user,
                template=template
            )
            mail_message.save()
            for subscriber in subscribers:
                recipient_email = subscriber.email
                recipient_name = subscriber.name
                
                context['recipient_email'] = recipient_email
                context['recipient_name'] = recipient_name

                html_content = render_to_string(f"newsletter/templates/{template}.html", context=context)
                text_content = strip_tags(html_content)

                email = EmailMultiAlternatives(
                    subject,
                    text_content,
                    EMAIL_HOST_USER,
                    [recipient_email]  # Send email to individual recipient
                )

                email.attach_alternative(html_content, 'text/html')
                email.send()

        messages.info(request, "Emails Sent Successfully")
        return redirect('subscribe:index')

    context = { 
        'title': 'Send Email to Subscribers'
    }
    return render(request, 'newsletter/send_email.html', context)
