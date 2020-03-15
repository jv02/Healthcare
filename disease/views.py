from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Patient,Doctor,Disease
from disease.models import  Relation,Record

# Create your views here.

def visu(request):

    """
    aadhar = request.POST['aadhar']
    passw = request.POST['password']
    doc= Doctor.objects.all().get(aadharno=aadhar)
    if doc.password == passw:
        res = render(request, 'home/dashboard.html', {'info': doc})
        res.set_cookie('aadhar', aadhar)
        return res
    else:
        return redirect('home:home')
    r = Record.objects.all().filter(disid__disname='pneumonia')
    r[2].aadharp.pincode

    """


    #rec=Disease.objects.filter(disname='pneumonia')
    r = Record.objects.all().filter(disid__disname='pneumonia')
    r1=[]
    for i in range(len(r)):
        if((str(r[i])[8:10])=='27'):
            r1.append(r[i])
    r4=[]
    for i in range(len(r)):
        if(str(r[i])[8:10]=='24'):
            r4.append(r[i])
    r3 = []
    for i in range(len(r)):
        if (str(r[i])[8:10] == '25'):
            r3.append(r[i])
    r2=[]
    for i in range(len(r)):
        if(str(r[i])[8:10]=='26'):
            r2.append(r[i])

    p = []
    for i in range(64):
        p.append(0.1)
    for i in range(len(r)):
        t=r[i].aadharp.pincode
        p[t-1]=1+p[t-1]
    maxx=max(p)
    min=0
    for i in range(len(p)):
        p[i]=(p[i]/maxx)
        if(p[i]<0.1):
            p[i]=0.1

    p2=[]
    for i in range(17):
        p2.append(0.1)
    for i in range(len(r2)):
        t=r2[i].aadharp.pincode
        p2[t-1]=1+p2[t-1]
    maxx=max(p2)
    min=0
    for i in range(len(p2)):
        p2[i]=(p2[i]/maxx)
        if(p2[i]<0.1):
            p2[i]=0.1

    p3=[]
    for i in range(17):
        p3.append(0.1)
    for i in range(len(r3)):
        t=r3[i].aadharp.pincode
        p3[t-1]=1+p3[t-1]
    maxx=max(p3)
    min=0
    for i in range(len(p3)):
        p3[i]=(p3[i]/maxx)
        if(p3[i]<0.1):
            p3[i]=0.1

    p4=[]
    for i in range(17):
        p4.append(0.1)
    for i in range(len(r4)):
        t=r4[i].aadharp.pincode
        p4[t-1]=1+p2[t-1]
    maxx=max(p4)
    min=0
    for i in range(len(p4)):
        p4[i]=(p4[i]/maxx)
        if(p4[i]<0.1):
            p4[i]=0.1

    d = Disease.objects.all()
    return render(request, 'disease/visualization.html',{'p1':0.3,'p2_1':p2,
                                                         'p2': 0.4,'p3_1':p3,
                                                         'p3': 0.5,'p4_1':p4,
                                                         'p4': 0.6,
                                                         'p5': 0.7,
                                                         'p6': 0.8,
                                                         'p7': 0.7,
                                                         'p8': 0.6,
                                                         'p9': 0.5,
                                                         'p10': p[9],
                                                         'p11': p[10],
                                                         'p12': p[11],
                                                         'p13': p[12],
                                                         'p14': p[13],
                                                         'p15': p[14],
                                                         'p16': p[15],
                                                         'p17': p[16],
                                                         'p18': p[17],
                                                         'p19': p[18],
                                                         'p20': p[19],
                                                         'p21': p[20],
                                                         'p22': p[21],
                                                         'p23': p[22],
                                                         'p24': p[23],
                                                         'p25': p[24],
                                                         'p26': p[25],
                                                         'p27': p[26],
                                                         'p28': p[27],
                                                         'p29': p[28],
                                                         'p30': p[29],
                                                         'p31': p[30],
                                                         'p32': p[31],
                                                         'p33': p[32],
                                                         'p34': p[33],
                                                         'p35': p[34],
                                                         'p36': p[35],
                                                         'p37': p[36],
                                                         'p38': p[37],
                                                         'p39': p[38],
                                                         'p40': p[39],
                                                         'p41': p[40],
                                                         'p42': p[41],
                                                         'p43': p[42],
                                                         'p44': p[43],
                                                         'p45': p[44],
                                                         'p46': p[45],
                                                         'p47': p[46],
                                                         'p48': p[47],
                                                         'p49': p[48],
                                                         'p50': p[49],
                                                         'p51': p[50],
                                                         'p52': p[51],
                                                         'p53': p[52],
                                                         'p54': p[53],
                                                         'p55': p[54],
                                                         'p56': p[55],
                                                         'p57': p[56],
                                                         'p58': p[57],
                                                         'p59': p[58],
                                                         'p60': p[59],
                                                         'p61': p[60],
                                                         'p62': p[61],
                                                         'p63': p[62],
                                                         'p64': p[63],

                                                         "data": d
                                                         })

