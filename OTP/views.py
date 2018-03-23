# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import jwt
import urllib2
import json
import random
# Create your views here.

@csrf_exempt
def verifyOtp(request):
	if request.method == "POST":

		otp = request.POST.get("otp")
		authKey = "176332A81pH4L759c8aad6"
		mobile = request.POST.get("number")

		print(mobile)

		token = request.POST.get("token")

		print(token)

		verifyOtpUrl = "https://control.msg91.com/api/verifyRequestOTP.php?authkey="+authKey+"&mobile=91"+str(mobile)+"&otp="+str(otp)+""

		response = urllib2.urlopen(verifyOtpUrl).read()

		response = json.loads(response)
		print(response)	



		if response['type'] == 'success':
			data = {
				"success" : True,
				"message" : "Number verified"
			}

		else:
			data = {
				"success" : False,
				"message" : "Number verification failed"
			} 	

		return JsonResponse(data,safe=False)