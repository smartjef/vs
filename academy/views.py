from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request, unit_slug=None, school_slug=None):
    school=None
    title = "Notes"
    schools = School.objects.filter(is_active=True)
    unit_names = UnitName.objects.filter(is_active=True)
    notes = Note.objects.filter(is_active=True)
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(is_active=True, file__icontains=query) or Note.objects.filter(is_active=True, unit_name__title__icontains=query) or Note.objects.filter(is_active=True, school__title__icontains=query) or Note.objects.filter(is_active=True, user__first_name__icontains=query)
        title = f"{notes.count()} Note(s) matching the query {query}"

    if unit_slug:
        unit = get_object_or_404(UnitName, is_active=True, slug=unit_slug)
        notes = Note.objects.filter(is_active=True, unit_name=unit)
        title = f"Notes under unit {unit}"

    if school_slug:
        school = get_object_or_404(School, is_active=True, slug=school_slug)
        notes = Note.objects.filter(is_active=True, school=school)
        title = f"Notes under school {school}"

    context = {
        'notes': notes,
        'schools': schools,
        'units': unit_names,
        'school':school,
        'title': title
    }

    return render(request, 'edu/index.html', context)

@login_required
def resources(request):
    return redirect('edu:index')