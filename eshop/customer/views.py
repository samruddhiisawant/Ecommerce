from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def customer(request):
    context={}
    return render(request, 'customer/starter.html')


def login(request):
    context = {}
    return render(request, 'customer/custom-login.html', context)
