from . import views
from django.urls import path

app_name = 'edu'

urlpatterns =[
    path('', views.index, name='index'),
    path('schools/<slug:school_slug>/', views.index, name='notes_by_school'),
    path('units/<slug:unit_slug>/', views.index, name='notes_by_unit'),
    path('resources/', views.resources, name='resources'),
    path('notes/my/', views.myDocuments, name="my-documents"),
    path('notes/add/', views.add_notes, name="add_notes"),
    path('notes/<int:note_id>/toggle-status/', views.toggle_status, name='toggle_status'),
    path('notes/<int:note_id>/delete/', views.note_delete, name='note_delete'),
]