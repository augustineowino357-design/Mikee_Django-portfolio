from django.shortcuts import get_object_or_404, render
from .models import Project

def portfolio_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/portfolio_index.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
