from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html', context={'Name': 'sandy', 'Age': '24'})


def users(request):
    return render(request, 'content.html')


def mustang(request):
    return render(request, 'content1.html')


def rrm(request):
    return render(request, 'rrmtc.html')


def csb(request):
    return render(request, 'csb.html')


def signin(request):
    return render(request, 'signinpage.html')


def oxw(request):
    return render(request, 'oxw.html')


def tom(request):
    return render(request, 'tom.html')


def vbm(request):
    return render(request, 'vbm.html')


def ism(request):
    return render(request, 'ism.html')


def contact(request):
    return render(request, 'contact.html')


