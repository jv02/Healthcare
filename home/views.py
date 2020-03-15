from django.http import HttpResponse
from django.shortcuts import render
from account.models import Patient


def homepage(request):
    return render(request, 'home/index.html')


def detail(request,id):
    p=Patient.objects.all().get(aadhar_no=id)
    return render(request,"home/dashboard.html",{"data":p})


