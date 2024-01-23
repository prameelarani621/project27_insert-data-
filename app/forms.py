from django import forms
from app.models import *


class Topicforms(forms.Form):
    topic_name=forms.CharField()



class WebPageform(forms.Form):
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()


class AcessRecordforms(forms.Form):
    wl=[[wo.pk,wo.name] for wo in WebPage.objects.all()]
    name=forms.ChoiceField(choices=wl)
    data=forms.DateField()
    auther=forms.CharField()

class dept(forms.Form):
    deptno=forms.IntegerField()
    dname=forms.CharField()
    loc=forms.CharField()


# class emp(forms.Form):
    # dl=[[do.deptno,do.empno] for do in dept.objects.all()]
