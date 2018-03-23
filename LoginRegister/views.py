# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import jwt
import urllib2
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import random
from .models import CompanyDetails ,UserDetail
# Create your views here.

def index(request):
    return render(request , 'index.html')

def registration(request):
    company = CompanyDetails.objects.values('company').distinct()
    return render(request, 'register.html',{'company':company})

def companyList(request):
    company = CompanyDetails.objects.values('company').distinct()
    print(company)
    companyList = []

    for obj in company:
        tempData = obj['company']
        companyList.append(tempData)
        tempData = {}

    data = {}
    data['success'] = True
    data['company'] = companyList

    return JsonResponse(data,safe=False)    

@csrf_exempt
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        pincode = request.POST.get('pincode')
        model = request.POST.get('model')
        company = request.POST.get('company')

        userDetailObj = UserDetail.objects.create(
            name=name,
            mobile=mobile,
            pincode=pincode,
            model=model,
            company=company
        )

        authKey = "176332A81pH4L759c8aad6"
        senderId = "CodeSVS"
        otp = random.randint(2000,9999)

        print(otp)

        try:
            sendOtpUrl = "https://control.msg91.com/api/sendotp.php?authkey="+authKey+"&mobile=91"+str(mobile)+"&message=Your%20otp%20is%20"+str(otp)+"&sender="+senderId+"&otp="+str(otp)+""

            response = urllib2.urlopen(sendOtpUrl).read()

            print(response)

        except Exception as e:
            print(str(e))
            data['success'] = False
            data['message'] = "Otp not sent"

            return JsonResponse(data,safe=False)

        data = {}
        data['success'] = True
        data['message'] = "User Registered"

        return JsonResponse(data,safe=False)

        

