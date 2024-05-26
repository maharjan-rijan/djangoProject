from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import usersForm
from service.models import Service

# def homePage(request):
#     data={
#         'title':'Home Page',
#         'bdata':'Welcome to kathmandu BernHardt College',
#         'client':['PHP','JAVA','CSS'],
#         'numbers':[ ],
#         'sDetails':[
#             {'name':'Sunaina Maharjan', 'contact':9863330824},
#             {'name':'Rijan Maharjan', 'contact':9866293218}
#         ]
#     }
#     return render(request,"index.html",data)

def mainPage(request):
    servicesData=Service.objects.all().order_by('-service_title')[:6]
    data={
        'servicesData':servicesData
    }
    return render(request,"index.html",data)

def events(request):
    return render(request,"events.html")

def gallery(request):
    return render(request,"gallery.html")

def our_story(request):
    return render(request,"our-story.html")

def contact(request):
    try:
        if request.method=="POST":
            n=request.POST.get('name')
            n1=request.POST.get('email')
            print(n + n1)
    except:
        pass
    return render(request,"contact.html")

def calculator(request):
    c=' '
    try:
        if request.method=="POST":
            num1=eval(request.POST.get('n1'))
            num2=eval(request.POST.get('n2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=num1+num2
            elif opr=="-":
                c=num1-num2
            elif opr=="*":
                c=num1*num2
            elif opr=="/":
                c=num1/num2
    except:
        c="Invalid Operation .............."
    return render(request,"calculator.html",{'c':c})

def evenOdd(request):
    c=''
    if request.method=="POST":
        if request.POST.get('n1')==" ":
            return render(request,"evenodd.html",{'error':True})
        
        n=eval(request.POST.get('n1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
    return render(request,"evenodd.html",{'c':c})

def form(request):
    finalans=0
    fn = usersForm()
    data={'form':fn}
    try:
        if request.method=="POST":
            n=int(request.POST.get('num1'))
            n1=int(request.POST.get('num2'))
            finalans=n+n1
            data={'form':fn,
                  'output': finalans
                  }
            
            url="/events/?output={}".format(finalans)
            return redirect(url)
    except:
        pass
    return render(request, "userform.html",data)

def submitForm(request):
    return HttpResponse(request)

def marksheet(request):
    if request.method=="POST":
        sub1=eval(request.POST.get('subject1'))
        sub2=eval(request.POST.get('subject2'))
        sub3=eval(request.POST.get('subject3'))
        sub4=eval(request.POST.get('subject4'))
        sub5=eval(request.POST.get('subject5'))
        t=sub1+sub2+sub3+sub4+sub5
        
        p=t*100/500
        if p>=60:
            d="First Division"
        elif p>=48:
            d="Second Division"
        elif p>=35:
            d="Third Division"
        else:
            d="Fail"
        data={
            'total':t,
            'percentage':p,
            'division':d
        }
        return render(request, "marksheet.html",data)
    return render(request,"marksheet.html")