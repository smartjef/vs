from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Profile
from django.contrib.auth.models import User
from random import randrange
def index(request):
    context = {
        'title': 'Get Work Done',
    }
    return render(request, 'assignments/index.html', context)

@login_required
def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'assignments/dashboard.html', context)

@login_required
def referals(request):
    context = {
        'title': 'Referals',
    }
    return render(request, 'assignments/referals.html', context)

@login_required
def orders(request):
    context = {
        'title': 'Orders',
    }
    return render(request, 'assignments/orders.html', context)

@login_required
def earnings(request):
    context = {
        'title': 'Earnings',
    }
    return render(request, 'assignments/earnings.html', context)

@login_required
def withdrawals(request):
    context = {
        'title': 'Withdrawals',
    }
    return render(request, 'assignments/withdrawals.html', context)

@login_required
def place_an_order(request):
    context = {
        'title': 'Place an Order',
    }
    return render(request, 'assignments/place_an_order.html', context)

def generate_unique_code():
    alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y','Z']
    char1 = alphabets[randrange(0,25,1)]
    char2 = alphabets[randrange(0,25,1)]
    char3 = alphabets[randrange(0,25,1)]
    new_code = f'VS-{char1}{char2}{char3}'
    return new_code

@login_required
def generate_code(request, user_id):
    if request.user == get_object_or_404(User, id=user_id):
        profile = get_object_or_404(Profile, user=request.user)
        if profile.code != None:
            messages.info(request, f'You already have referal code, your Code is {profile.code}')
        else:
            new_code = generate_unique_code()
            if Profile.objects.filter(code=new_code).exists():
                new_code = generate_code()
            profile.code = new_code
            profile.save()
            messages.success(request, f'Code generated successfully, your Code is {new_code}')
    else:
        messages.warning(request, f'Unautherized Operation')
    return redirect('gwd:dashboard')