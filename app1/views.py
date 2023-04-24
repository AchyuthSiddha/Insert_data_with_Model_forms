from django.shortcuts import render

from django.http import HttpResponse
from app1.forms import *
# Create your views here.
def Insert_Topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFOD=TopicForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
            return HttpResponse("data inserted Sucessfully in Topic")
    return render(request,'Insert_Topic.html',d)


def Insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFOD=WebpageForm(request.POST)
        if WFOD.is_valid():
            WFOD.save()
            return HttpResponse("data inserted Sucessfully in Topic")
    return render(request,'Insert_webpage.html',d)

def Insert_Access_record(request):
    AFO=Access_RecordForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AFOD=Access_RecordForm(request.POST)
        if AFOD.is_valid():
            AFOD.save()
            return HttpResponse("data inserted Sucessfully in Topic")
    return render(request,'Insert_Access_record.html',d)
