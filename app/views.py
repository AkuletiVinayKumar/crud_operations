from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn = input("Enter Topic Name")
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("Topic is inserted successfully")

def insert_webpage(request):
    tn = input("Enter topic_name")
    n = input("Enter name")
    url = input("enter url")
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO =Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse("Web page data is inserted")

def insert_AccessRecord(request):
    tn = input("Enter topic_name")
    n = input("Enter name")
    url = input("enter url")
    A = input("enter Author")
    D = input("enter date")
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO =Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    
    AO = AccessRecord.objects.get_or_create(name=WO,author=A,date=D)[0]
    


def display_topics(request):
    LOT = Topic.objects.all()
    d = {'topics' : LOT }
    return render(request,'display_topics.html',context = d)

def display_webpage(request):
    LOW = Webpage.objects.all()
    d= {'webpages' : LOW}
    return render(request,'display_webpage.html',context=d)

def display_access(request):
    LOA = AccessRecord.objects.all()
    d = {'access':LOA}
    return render (request,'display_access.html',context=d)
