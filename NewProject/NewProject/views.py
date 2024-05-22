from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    return render(request,"index.html")

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

def form(request):
    finalans=0
    try:
        if request.method=="POST":
            n=int(request.POST.get('num1'))
            n1=int(request.POST.get('num2'))
            finalans=n+n1
            
            url="/events/?output={}".format(finalans)
            return redirect(url)
    except:
        pass
    return render(request, "form.html",{'output':finalans})

def submitForm(request):
    return HttpResponse(request)
