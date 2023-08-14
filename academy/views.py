from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
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

@login_required
def myDocuments(request):
    notes = Note.objects.filter(user=request.user)
    schools = School.objects.filter(is_active=True)
    unit_names = UnitName.objects.filter(is_active=True)
    context = {
        'notes': notes,
        'schools': schools,
        'units': unit_names,
        'title': "My Documents"
    }
    return render(request, 'edu/my-documents.html', context)

@login_required
def add_notes(request):
    schools = School.objects.filter(is_active=True)
    unit_names = UnitName.objects.filter(is_active=True)
    context = {
        'title': "Add Documents",
        'schools': schools,
        'units': unit_names,
    }
    return render(request, 'edu/add-notes.html', context)

@login_required
def toggle_status(request, note_id):
    note = get_object_or_404(Note, user=request.user, id=note_id)
    if note.is_active:
        note.is_active = False
        note.save()
        messages.success(request, f'{note} Unpublished Succesfully.')
        return redirect('edu:my-documents')
    else:
        note.is_active = True
        note.save()
        messages.success(request, f'{note} Published Succesfully.')
        return redirect('edu:my-documents')
    
@login_required    
def note_delete(request, note_id):
    note = get_object_or_404(Note, user=request.user, id=note_id)
    if note.file:
        note.file.delete()
    note.delete()

    messages.success(request, f'Note Deleted Succesfully.')
    return redirect('edu:my-documents')
