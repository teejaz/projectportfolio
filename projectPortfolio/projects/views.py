from django.shortcuts import HttpResponse


def projects(request):
    return HttpResponse("projects go here")


def home(request):
    return HttpResponse("this is main page")
