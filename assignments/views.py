from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Referal, AssignmentOrder, ProjectOrder, Period, AssignmentFiles, Payment, ProjectFiles, ProjectPeriod
from ai.models import IdeaRequest, GeneratedIdeas, AreaChoice,LevelChoice
from random import randrange
from collections import defaultdict
from datetime import date, timedelta

def index(request):
    context = {
        'title': 'Get Work Done',
    }
    return render(request, 'assignments/index.html', context)

@login_required
def dashboard(request):
    data = []
    label = []
    start_date = date.today() - timedelta(days=365)

    ideas_referal = IdeaRequest.objects.filter(payment__is_paid=True, refered_by=request.user)
    assignment_referal = AssignmentOrder.objects.filter(refered_by=request.user, status='Completed')
    project_referal = ProjectOrder.objects.filter(refered_by=request.user, status='Completed')
    all_orders = list(ideas_referal) + list(assignment_referal) + list(project_referal)
    total_referals = ideas_referal.count()+assignment_referal.count()+project_referal.count()
    current_date = start_date
    month_counter = 0

    while month_counter < 13:
        month_name = current_date.strftime('%b')
        year = current_date.year
        orders_for_month = [order for order in all_orders if order.created_at.month == current_date.month and order.created_at.year == year]
        month_earnings = sum(order.payment.get_amount_earned_by_referer() for order in orders_for_month)
        
        if month_counter > 0:
            label.append(month_name)
            data.append(month_earnings)
        
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)
        
        month_counter += 1
    completed_orders = ProjectOrder.objects.filter(user=request.user, status="Completed").count()+AssignmentOrder.objects.filter(user=request.user, status="Completed").count()+IdeaRequest.objects.filter(user=request.user, is_active=True).count()
    cancelled_orders = ProjectOrder.objects.filter(user=request.user, status="Cancelled").count()+AssignmentOrder.objects.filter(user=request.user, status="Cancelled").count()+IdeaRequest.objects.filter(user=request.user, is_active=False).count()
    pending_orders = ProjectOrder.objects.filter(user=request.user, status="Pending").count()+AssignmentOrder.objects.filter(user=request.user, status="Pending").count()
    context = {
        'title': 'Dashboard',
        'total_referal': total_referals,
        'completed_orders': completed_orders,
        'cancelled_orders': cancelled_orders,
        'pending_orders': pending_orders,
        'data': data,
        'label': label
    }
    return render(request, 'assignments/dashboard.html', context)

@login_required
def referals(request):
    ideas_referal = IdeaRequest.objects.filter(payment__is_paid=True, refered_by=request.user)
    assignment_referal = AssignmentOrder.objects.filter(refered_by=request.user, status='Completed')
    project_referal = ProjectOrder.objects.filter(refered_by=request.user, status='Completed')
    total_referals = ideas_referal.count() + assignment_referal.count() + project_referal.count()
    context = {
        'title': 'Referals',
        'total_referal': total_referals,
        'idea_referal': ideas_referal,
        'assignment_referal': assignment_referal,
        'project_referal': project_referal
    }
    return render(request, 'assignments/referals.html', context)

@login_required
def orders(request):
    idea_requests = IdeaRequest.objects.filter(user=request.user, is_active=True)
    projects = ProjectOrder.objects.filter(user=request.user)
    assignments = AssignmentOrder.objects.filter(user=request.user)
    completed_orders = ProjectOrder.objects.filter(user=request.user, status="Completed").count()+AssignmentOrder.objects.filter(user=request.user, status="Completed").count()+IdeaRequest.objects.filter(user=request.user, is_active=True).count()
    cancelled_orders = ProjectOrder.objects.filter(user=request.user, status="Cancelled").count()+AssignmentOrder.objects.filter(user=request.user, status="Cancelled").count()+IdeaRequest.objects.filter(user=request.user, is_active=False).count()
    pending_orders = ProjectOrder.objects.filter(user=request.user, status="Pending").count()+AssignmentOrder.objects.filter(user=request.user, status="Pending").count()
    total_orders = completed_orders + cancelled_orders + pending_orders
    context = {
        'title': 'Orders',
        'idea_requests':idea_requests,
        'projects': projects,
        'assignments': assignments,
        'total_orders': total_orders,
        'completed_orders': completed_orders,
        'cancelled_orders': cancelled_orders,
        'pending_orders': pending_orders
    }
    return render(request, 'assignments/orders.html', context)

@login_required
def earnings(request):
    data = []
    label = []
    start_date = date.today() - timedelta(days=365)

    ideas_referal = IdeaRequest.objects.filter(payment__is_paid=True, refered_by=request.user)
    assignment_referal = AssignmentOrder.objects.filter(refered_by=request.user, status='Completed')
    project_referal = ProjectOrder.objects.filter(refered_by=request.user, status='Completed')
    all_orders = list(ideas_referal) + list(assignment_referal) + list(project_referal)
    total_referals = ideas_referal.count()+assignment_referal.count()+project_referal.count()
    current_date = start_date
    month_counter = 0

    while month_counter < 13:
        month_name = current_date.strftime('%b')
        year = current_date.year
        orders_for_month = [order for order in all_orders if order.created_at.month == current_date.month and order.created_at.year == year]
        month_earnings = sum(order.payment.get_amount_earned_by_referer() for order in orders_for_month)
        
        if month_counter > 0:
            label.append(month_name)
            data.append(month_earnings)
        
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)
        
        month_counter += 1

    context = {
        'title': 'Earnings',
        'total_referal': total_referals,
        'earnings':all_orders,
        'data': data,
        'label': label
    }
    return render(request, 'assignments/earnings.html', context)

@login_required
def withdrawals(request):
    total_referals = IdeaRequest.objects.filter(payment__is_paid=True, refered_by=request.user).count() + AssignmentOrder.objects.filter(refered_by=request.user, status='Completed').count() + ProjectOrder.objects.filter(refered_by=request.user, status='Completed').count()
    context = {
        'title': 'Withdrawals',
        'total_referal': total_referals
    }
    return render(request, 'assignments/withdrawals.html', context)

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
    messages.success(request, f'Successfully deleted {idea}!')
    return redirect('gwd:request_detail', idea.idea_request.id)

@login_required
def idea_detail(request, idea_id):
    idea = get_object_or_404(GeneratedIdeas, id=idea_id, idea_request__user=request.user)
    context = {
        'title': f'{idea}',
        'idea':idea
    }
    return render(request, 'assignments/idea_detail.html', context)

@login_required
def project_detail(request, project_id):
    obj = get_object_or_404(ProjectOrder, id=project_id, user=request.user)
    context = {
        'title': obj.title,
        'category': 'Project - GWD',
        'category_url_': reverse('gwd:orders'),
        'obj': obj
    }
    return render(request, 'assignments/order-details.html', context)

@login_required
def assignment_detail(request, assignment_id):
    obj = get_object_or_404(AssignmentOrder, id=assignment_id, user=request.user)
    context = {
        'title': obj.title,
        'category': 'Assignments - GWD',
        'category_url_': reverse('gwd:orders'),
        'obj': obj
    }
    return render(request, 'assignments/order-details.html', context)

@login_required
def AssignmentOrderCreateView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        academic_level_id = request.POST.get('academic_level')
        subject_area_id = request.POST.get('subject_area')
        period_id = request.POST.get('period')
        additional_information = request.POST.get('additional_information')
        referal_code = request.POST.get('referal_code')
        user = request.user
        refered_by = None
        subject_area = None
        academic_level = LevelChoice.objects.get(id=academic_level_id)
        period = Period.objects.get(id=period_id)
        if subject_area_id:
            subject_area = AreaChoice.objects.get(id=subject_area_id)

        if referal_code:
            if Referal.objects.filter(code=referal_code).exists():
                referal = Referal.objects.get(code=referal_code)
                refered_by = referal.user
            else:
                messages.warning(request, 'Invalid Referal Code!')
                return redirect('gwd:leave_assignment')
        files = request.FILES.getlist('files')

        if not files and not additional_information:
            messages.warning(request, 'Provide additional Information or attach Assignment File(s)!')
            return redirect('gwd:leave_assignment')
        
        assignment = AssignmentOrder.objects.create(
            user=user,
            title=title,
            academic_level=academic_level,
            subject_area=subject_area,
            period=period,
            additional_information=additional_information,
            refered_by=refered_by
        )

        for f in files:
            assignment_file = AssignmentFiles.objects.create(assignment=assignment, file=f)
            assignment_file.save()
        payment = Payment.objects.create(assignment=assignment, transaction_code=generate_unique_code(), amount=assignment.get_amount())
        payment.save()
        messages.success(request, 'Assignment and files successfully submitted.')
        return redirect('gwd:make_payment', payment.transaction_code)
    else:
        context = {
            'title':'Leave An Assignment',
        }
        return render(request, 'assignments/leave-assignment.html', context)

@login_required
def ProjectOrderCreateView(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        academic_level_id = request.POST.get('academic_level')
        subject_area_id = request.POST.get('subject_area')
        period_id = request.POST.get('period')
        additional_information = request.POST.get('additional_information')
        referal_code = request.POST.get('referal_code')
        user = request.user
        refered_by = None
        subject_area = None
        academic_level = LevelChoice.objects.get(id=academic_level_id)
        period = ProjectPeriod.objects.get(id=period_id)
        if subject_area_id:
            subject_area = AreaChoice.objects.get(id=subject_area_id)

        if referal_code:
            if Referal.objects.filter(code=referal_code).exists():
                referal = Referal.objects.get(code=referal_code)
                refered_by = referal.user
            else:
                messages.warning(request, 'Invalid Referal Code!')
                return redirect('gwd:leave_project')
            
        files = request.FILES.getlist('files')

        if not files and not additional_information:
            messages.warning(request, 'Provide additional Information or attach project File(s)!')
            return redirect('gwd:leave_project')

        project = ProjectOrder.objects.create(
            user=user,
            title=title,
            academic_level=academic_level,
            subject_area=subject_area,
            period=period,
            additional_information=additional_information,
            refered_by=refered_by
        )

        for f in files:
            project_file = ProjectFiles.objects.create(project=project, file=f)
            project_file.save()
        payment = Payment.objects.create(project=project, transaction_code=generate_unique_code(), amount=project.get_amount())
        payment.save()
        messages.success(request, 'Project and files successfully submitted.')
        return redirect('gwd:make_payment', payment.transaction_code)
    else:
        context = {
            'title':'Leave A Project',
        }
        return render(request, 'assignments/leave-project.html', context)

@login_required    
def payment(request, code):
    payment = get_object_or_404(Payment, transaction_code=code)

    title = f"Make payment of {payment.amount}"
    if payment.is_paid:
        title = f'Payment of Ksh. {payment.amount} Completed'

    context = {
        'title' : title,
        'payment': payment
    }
    return render(request, 'assignments/make_payment.html', context)





