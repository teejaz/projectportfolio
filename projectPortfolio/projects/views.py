from django.shortcuts import render, get_object_or_404
from .models import Project
from rest_framework import generics
from .serializer import ProjectSerializer
import requests


def home(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects': projects})


def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project': project_detail})


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
