from django.shortcuts import HttpResponse, render


def projects(request):
    return HttpResponse("projects go here")


def home(request):
    return render(request, 'projects/home.html')
