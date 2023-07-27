from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Profile
from .models import Referal
from ai.models import IdeaRequest, GeneratedIdeas
from django.contrib.auth.models import User
from random import randrange
def index(request):
    context = {
        'title': 'Get Work Done',
    }
    return render(request, 'assignments/index.html', context)

@login_required
def dashboard(request):
    ideas_referal = IdeaRequest.objects.filter(payment__is_paid=True, refered_by=True).count()
    assignment_referal = 15
    project_referal = 10
    total_referals = ideas_referal + assignment_referal + project_referal
    context = {
        'title': 'Dashboard',
        'total_referal': total_referals
    }
    return render(request, 'assignments/dashboard.html', context)

@login_required
def referals(request):
    ideas_referal = IdeaRequest.objects.filter(payment__is_paid=True, refered_by=True)
    assignment_referal = 15
    project_referal = 10
    total_referals = ideas_referal.count() + assignment_referal + project_referal
    context = {
        'title': 'Referals',
        'total_referal': total_referals,
        'idea_referal': ideas_referal,
    }
    return render(request, 'assignments/referals.html', context)

@login_required
def orders(request):
    idea_requests = IdeaRequest.objects.filter(user=request.user, is_active=True)
    context = {
        'title': 'Orders',
        'idea_requests':idea_requests
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
def generate_code(request):
    referal = Referal.objects.filter(user=request.user)
    if referal.exists():
        code = request.user.referal.code
        messages.info(request, f'You already have referal code, your Code is {code}')
    else:
        new_code = generate_unique_code()
        if Referal.objects.filter(code=new_code).exists():
            new_code = generate_code()
        new_referal = Referal.objects.create(
            user = request.user,
            code = new_code
        )
        new_referal.save()
        messages.success(request, f'Code generated successfully, your Code is {new_code}')
    return redirect('gwd:dashboard')


@login_required
def idea_request_detail(request, id):
    idea_request = get_object_or_404(IdeaRequest, id=id, user=request.user, is_active=True)
    context = {
        'title': 'Idea Request Detail',
        'idea_request':idea_request
    }
    return render(request, 'assignments/ideas_detail.html', context)

@login_required
def idea_request_delete(request, id):
    idea_request = get_object_or_404(IdeaRequest, id=id, user=request.user, payment__is_paid=True, is_active=True)
    idea_request.is_active = False
    idea_request.save()
    messages.success(request, 'Idea Request Deleted Successfully')
    return redirect('gwd:ideas')

@login_required
def idea_delete(request, idea_id):
    idea = get_object_or_404(GeneratedIdeas, id=idea_id, idea_request__user=request.user)
    idea.delete()
    messages.success(request, f'Successfully deleted {idea.title}!')
    return redirect('gwd:request_detail', idea.idea_request.id)

@login_required
def idea_detail(request, idea_id):
    idea = get_object_or_404(GeneratedIdeas, id=idea_id, idea_request__user=request.user)
    context = {
        'title': f'{idea.title}',
        'idea':idea
    }
    return render(request, 'assignments/idea_detail.html', context)