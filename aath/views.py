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

def service_psychiatric_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"service.html",{"msg":msg})

def contact(request):
    msg=request.GET.get("msg",'')
    return render(request,"contact.html",{"msg":msg})

def family_therappy_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"familytherapy.html",{"msg":msg})

def child_guidance_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"childguidence.html",{"msg":msg})

def anxiety_depression_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"anxietydisorder.html",{"msg":msg})

def phobia_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"phobiasdepression.html",{"msg":msg})

def depression_treatment_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"depression.html",{"msg":msg})

def couple_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"couple.html",{"msg":msg})

def marriage_therappy_post_marriage_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"marriage.html",{"msg":msg})

def individual_personal_face_to_face_counseling_services_offered_by_aathmajyothi_for_bangalore_and_mysore(request):
    msg=request.GET.get("msg",'')
    return render(request,"individual.html",{"msg":msg})


