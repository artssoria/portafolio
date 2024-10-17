from django.shortcuts import render
from .models import Project

def porfolio(request):
    projects = Project.objects.all()
    return render(request, 'porfolio/portfolio.html',{'projects':projects})