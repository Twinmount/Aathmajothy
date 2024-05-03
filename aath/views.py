from django.shortcuts import render,redirect
import datetime
from datetime import date

# Create your views here.

def index(request):
    msg=request.GET.get("msg",'')
    return render(request,"index.html",{"msg":msg})

def about(request):
    msg=request.GET.get("msg",'')
    return render(request,"about.html",{"msg":msg})

def service(request):
    msg=request.GET.get("msg",'')
    return render(request,"service.html",{"msg":msg})

def contact(request):
    msg=request.GET.get("msg",'')
    return render(request,"contact.html",{"msg":msg})

def familythera(request):
    msg=request.GET.get("msg",'')
    return render(request,"familytherapy.html",{"msg":msg})

def childguide(request):
    msg=request.GET.get("msg",'')
    return render(request,"childguidence.html",{"msg":msg})

def anxiety(request):
    msg=request.GET.get("msg",'')
    return render(request,"anxietydisorder.html",{"msg":msg})

def phobia(request):
    msg=request.GET.get("msg",'')
    return render(request,"phobiasdepression.html",{"msg":msg})

def depression(request):
    msg=request.GET.get("msg",'')
    return render(request,"depression.html",{"msg":msg})

def couple(request):
    msg=request.GET.get("msg",'')
    return render(request,"couple.html",{"msg":msg})

def marriage(request):
    msg=request.GET.get("msg",'')
    return render(request,"marriage.html",{"msg":msg})

def individual(request):
    msg=request.GET.get("msg",'')
    return render(request,"individual.html",{"msg":msg})


