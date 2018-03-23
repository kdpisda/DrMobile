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
        print(obj)
        tempData = {
            "company":obj['company']
        }

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

        data = {}
        data['success'] = True
        data['message'] = "User Registered"

        return JsonResponse(data,safe=False)

        

