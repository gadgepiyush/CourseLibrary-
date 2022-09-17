from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def activities(request):
    return render(request, 'activities.html')


def contactus(request):
    return render(request, 'contactus.html')
