from django.urls import path
from . import views

app_name = 'gwd'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('referals/', views.referals, name='referals'),
    path('orders/', views.orders, name='orders'),
    path('requests/<int:id>/', views.idea_request_detail, name='request_detail'),
    path('requests/<int:id>/delete/', views.idea_request_delete, name='request_delete'),
    path('requests/ideas/<int:idea_id>/', views.idea_detail, name='ideas_detail'),
    path('requests/ideas/<int:idea_id>/delete/', views.idea_delete, name='ideas_delete'),
    path('earnings/', views.earnings, name='earnings'),
    path('withdrawals/', views.withdrawals, name='withdrawals'),
    path('get-code/', views.generate_code, name='get_code'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('leave-assignment/', views.AssignmentOrderCreateView, name='leave_assignment'),
    path('leave-project/', views.ProjectOrderCreateView, name='leave_project'),
    
]