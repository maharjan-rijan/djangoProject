from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request,"contact.html")