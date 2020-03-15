from django.shortcuts import render,redirect
from .models import Patient,Doctor
from disease.models import  Relation,Record,Disease
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def signup_p(request):
    t = Patient.objects.all() #take all details from patient
    return render(request, 'account/signup-pat.html',{})


def signup_pat(request):
    pat = Patient.objects.all()

    print("Hello form is submited")
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    aadhar = request.POST['aadhar']
    phone = request.POST['phone']
    password = request.POST['password']
    confirm = request.POST['confirm']
    aadhar = int(aadhar)
    t = False
    for i in pat:
        if i.aadhar_no == aadhar:
            t = True
            break

    if (t == False):
        patient = Patient(first_name=first_name, last_name=last_name, aadhar_no=aadhar, phone_no=phone,
                          password=password, conf_password=confirm)
        patient.save()

        return render(request, 'account/login-pat.html')
    else:
        return render(request, 'account/signup-pat.html',{'msg':t})


def login_p(request):
    return render(request, 'account/login-pat.html')


def login_pat(request):
    aadhar = request.POST['aadhar']
    passw = request.POST['password']
    patient = Patient.objects.all().get(aadhar_no=aadhar)
    if patient.password == passw:
        return render(request,'home/index.html',{'info':patient})
    else:
        return redirect('home:home')


def signup_d(request):
    return render(request, 'account/signup-doc.html',{})


def signup_doc(request):
    pat = Doctor.objects.all()

    print("Hello form is submited")
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    aadhar = request.POST['aadhar']
    phone = request.POST['phone']
    password = request.POST['password']
    confirm = request.POST['confirm']
    aadhar = int(aadhar)
    t = False
    for i in pat:
        if i.aadharno == aadhar:
            t = True
            break

    if (t == False):
        patient = Doctor(firstname=first_name, lastname=last_name, aadharno=aadhar, phoneno=phone,
                          password=password, confirmpassword=confirm)
        patient.save()
        return render(request, 'account/login-doc.html')
    else:
        return render(request, 'account/signup-doc.html',{'msg':t})


def login_d(request):
    return render(request, 'account/login-doc.html')


def login_doc(request):
    aadhar = request.POST['aadhar']
    passw = request.POST['password']
    doc= Doctor.objects.all().get(aadharno=aadhar)
    if doc.password == passw:
        res = render(request, 'home/dashboard.html', {'info': doc})
        res.set_cookie('aadhar', aadhar)
        return res
    else:
        return redirect('home:home')

def logout_doc(request):
    res = render(request, 'account/login-doc.html')
    res.delete_cookie('aadhar')
    return res

def pat_deatil(request):
    return render(request,'account/pat_details.html')

def show_patdetail(request):
    aadhar = request.POST['aadhar']
    aadhar1=int(aadhar)

    pat = Patient.objects.all().get(aadhar_no=aadhar1)
    r=Record.objects.all().filter(aadharp__aadhar_no=aadhar)

    return render(request,'account/show_patdetail.html',{'infopat':pat,'ra':r})


def record(request):
    d = Disease.objects.all()
    return render(request,'account/add_patient.html',{"data":d})


def record_process(request):
    pat = int(request.POST['aadhar'])
    dis = request.POST['disease']
    doc = request.COOKIES['aadhar']
    #pat_obj = Patient.objects.all().get(aadhar_no=pat)
   # doc_obj = Doctor.objects.all().filter(aadharno=doc).first()
   # dis_obj = Disease.objects.all().filter(disname=dis).first()
    #print(pat)
    #print(doc)
    #print(dis)
    print(dis)
    return render(request,'account/message.html',{"data":pat})