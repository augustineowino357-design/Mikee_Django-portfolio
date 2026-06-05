from django.shortcuts import render
from .models import Project

def portfolio_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/portfolio_index.html', context)
