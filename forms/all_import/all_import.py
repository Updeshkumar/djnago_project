from django.shortcuts import render ,redirect
# from numpy import double
from rest_framework import serializers
from django.http import  JsonResponse,HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.db import IntegrityError
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta  ,date
from django.core.paginator import Paginator




import datetime
import requests
import json
import random 
import razorpay
# import qrcode
# import pandas as pd
import csv, io
import ast
import base64
import hashlib


from time import strptime
from account.models import *
from vehicle_owner.models import *
from driver.models import *
from df_user.models import *
from labour_contructor.models import *
from sub_contructor.models import *



from django.shortcuts import render , redirect
from django.contrib import messages
from django.forms import inlineformset_factory,modelformset_factory
from django.contrib.auth import login, authenticate ,logout as deauth
from django.contrib.auth.decorators import login_required
from io import BytesIO
from django.core.files.uploadedfile import  File
from PIL import Image , ImageDraw
from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from account.serializer import *


#### forms
from labour_contructor.forms import *
from vehicle_owner.forms import *
from driver.forms import *
from sub_contructor.forms import *







### RANDOM FUNC TO GET RANDOM VALUE FOR MTID
def random_number():
    r1 = random.randint(1000000000000000, 9999999999999999)
    return r1