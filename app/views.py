from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    ETFO=Topicforms()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TNFO=Topicforms(request.POST)
        if TNFO.is_valid():
            To=TNFO.cleaned_data['topic_name']
            to=Topic.objects.get_or_create(topic_name=To)[0]
            to.save()
            TO=Topic.objects.all()
            d1={'topics':TO}
            return render(request,'display_topic.html',d1)
        else:
            return HttpResponse(request,'not valid')

    return render(request,'insert_topic.html',d)



def insert_WebPages(request):
    EWFO=WebPageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebPageform(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            to=Topic.objects.get(topic_name=tn)
            n=WFDO.changed_data['name']
            u=WFDO.changed_data['url']
            e=WFDO.changed_data['email']
            wo=WebPage.objects.get_or_create(topic_name=to,Name=n,url=u,email=e)[0]
            wo.save()
            return HttpResponse(request,'display_webpages.html',d)
        else:
            return HttpResponse(request,'not valid')

    return render(request,'insert_WebPages.html',d)




def insert_AcessRecords(request):
    EAFO=Topicforms()
    d={'ETFO':EAFO}
    if request.method=='POST':
        AFDO=Topicforms(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            wo=WebPage.objects.get(name=n)
            d=AFDO.changed_data['date']
            a=AFDO.changed_data['auther']
            ao=AcessRecord.objects.get_or_create(name=wo,date=d,auther=a)[0]
            ao.save()
            return HttpResponse(request,'display_acessrecords.html',d)
        else:
            return HttpResponse(request,'not valid')

    return render(request,'insert_AcessRecords.html',d)