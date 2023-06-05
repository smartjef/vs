from django.shortcuts import render, redirect
from .models import Subscriber
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.
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