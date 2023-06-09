from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Team
# Create your views here.
def team(request):
    context = {
        'title': 'Team Members',
        'team': Team.objects.filter(is_active=True),
    }
    return render(request, 'users/team/index.html', context)

def team_details(request, slug):
    team = get_object_or_404(Team, slug=slug, is_active=True)
    if team.user.get_full_name():
        title = team.user.get_full_name()
    else:
        title = "No Name Provided"
    context = {
        'team': team,
        'title': title,
        'category': 'Team',
        'category_url': reverse('users:team')
    }
    return render(request, 'users/team/details.html', context)