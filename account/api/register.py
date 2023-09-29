from all_import.all_import import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from account.serializer import stateSerializer, districtSerializer, tahseelSerializer



# def send_otp(mobileNo,otpToSave):
#     url = f"http://103.16.101.52:80/sendsms/bulksms?username=oz07-way2it&password=Way2it14&type=0&dlr=1&destination="+ mobileNo +"&source=SDIRAM&message=%3C%23%3E%20"+otpToSave+"%20is%20the%20OTP%20for%20login%20to%20your%20Shadiram%20account.%20This%20OTP%20is%20valid%20for%2015%20minutes.%20For%20security%20reason%20do%20not%20share%20with%20anyone.%20Shadiram.in&entityid=1201159195926105040&tempid=1307165045918848353"
#     resp=requests.get(url)
#     return None

def send_otp(mobileNo,otpToSave):
    url = f"https://control.msg91.com/api/v5/otp?template_id=64ae465ed6fc050316082ec3&mobile=91{mobileNo}"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authkey": "399430AXHWNUNwrm64ae44f2P1"
    }

    response = requests.post(url, headers=headers)
    print(response.text)
    

# This method is use to send otp on mobile
@api_view(['POST'])
def send_otp_mobile(request):
    try:       
        mobileNo = request.data['mobileNo']
        
        if mobileNo == '1234567899':
            
            getuser = User.objects.filter(mobile_number=mobileNo).first()
            # gettoken = Token.objects.get(user=getuser).key
            otp = '1234'  # Set a fixed OTP for this specific number
            message = "OTP auto-verified for mobile number 1234567899"
            context={
            "status":True ,
            "data":{
                'otp':otp, 
                "message": message,
                #"Token": gettoken,
                                
                }
            }
            return JsonResponse(context)  
        if not User.objects.filter(mobile_number=mobileNo).exists():
            saveUser = User(mobile_number = mobileNo)
            saveUser.save()
            saveUser.set_password(mobileNo)
            saveUser.save()
        # Generate random otp
        otp=str(random.randint(1000 , 9999))
        # Send SMS
        message = "An Otp sent to your mobile number"
        User.objects.filter(mobile_number=mobileNo).update(otp= otp)
        send_otp(mobileNo , otp)
        context={
            "status":True ,
            "data":{
                'otp':otp, 
                "message": message ,
            }
        }
        return JsonResponse(context)  
    except Exception as e:
        context={
            "status":False ,
            "data":{
                'otp':"", 
                "message": f"{e}" ,

            }
        }
        return JsonResponse(context)
        
        
        
def msgverifyotp(mobile, otp):
    url = f"https://control.msg91.com/api/v5/otp/verify?otp={otp}&mobile=91{mobile}"

    headers = {
        "accept": "application/json",
        "authkey": "399430AXHWNUNwrm64ae44f2P1"
    }

    response = requests.get(url, headers=headers)

    return response.text

import ast




# This method is use to verify otp
@api_view(['POST'])
def verify_mobile_otp(request):
    try:   
        mobileNo = request.data["mobileNo"]
        otp = request.data["otp"]
        if mobileNo == '1234567899':
            
            getuser = User.objects.filter(mobile_number=mobileNo, otp=otp).first()
            gettoken = Token.objects.get(user=getuser).key
            otp = '1234'  # Set a fixed OTP for this specific number
            message = "OTP auto-verified for mobile number 1234567899"
            context={
                    "status":True ,
                        "data":{ 
                            "message": "OTP is verified" ,
                            "otp_matched": True ,
                            "is_type": True ,
                            "userType":  "heavy-vehicle",
                            "is_paid": True ,
                            "vehicle_id": 0 ,
                            
                            ### driver
                            "driver_id": 0 ,
                            "driverPayment": False , 

                            ## Labour
                            "labour_id":0 ,
                            "labourPayment": False ,
                            
                            
                            # sub-contrucotr
                            "subcontructor_id" : 0 ,
                            "subcontructorPayment" : False,

                            "amount": 0 ,
                            "name": "Test" ,


                            "accessToken": gettoken,
                            "mobileNo":  request.data['mobileNo'] ,
                                }
                    }
            return JsonResponse(context)
        
        
        
       

        if not User.objects.filter(mobile_number=request.data['mobileNo']).exists(): #if phone number does not exists
            context={
            "status":False ,
            "data":{
                "message": "Mobile Number is not registerd" ,
                "userType": "" ,
                "accessToken": "",
                "mobileNo":"" 
                
                    }
                }
            return JsonResponse(context)  
        # check user exists with otp
        if User.objects.filter(mobile_number=request.data['mobileNo']).exists():
            # Global Parameter
            is_type = False
            userType = ""
            is_paid = False 
            vehicle_id = 0
            amount = 0 
            driver_id = 0
            driverPayment = False 
            labour_id =0
            labourPayment=False
            subcontructor_id = 0
            subcontructorPayment = False
            
            
            name = ""
            msgcheckotp = msgverifyotp(mobileNo,int(otp))

            print('mydict',msgcheckotp)
            # {"request_id":"336771704e72353839373836","type":"success"}
            res = ast.literal_eval(msgcheckotp)
            if res["type"] == "success":
                userInfo = User.objects.filter(mobile_number=request.data['mobileNo']).first()
                name = userInfo.first_name if userInfo.first_name else ''
                print(userInfo)
                
                # Token 
                checking_token = Token.objects.filter(user=userInfo).first()
                if checking_token:
                    checking_token.delete()
                get_token=Token.objects.create(user=userInfo)        

                ### profile of all is common model for type of user            
                if profileofall.objects.filter(user=userInfo).exists():
                    is_type = True 
                    userType = profileofall.objects.filter(user=userInfo).first().role

                    ### start vehicle user #########################
                    

                    vup=vehicle_user_profile.objects.filter(user=userInfo).first()
                    if vehicle_payment.objects.filter(user=vup , status=True).exists():
                        is_paid = True 

                    hv_obj = heavyvehivalregistration.objects.filter(user = vup).last()
                    if hv_obj:
                        vehicle_id = hv_obj.id    
                        amount=vehicle_payment_amount.objects.last().value   

                    ##### End vehicle user
                    
                    
                    
                    ################# start driver user #########################
                    if driver_profile.objects.filter(user=userInfo).exists():

                        driver_prof=driver_profile.objects.filter(user=userInfo).first()

                        if driver_prof:
                            driver_id = driver_prof.id 
                            amount=driver_payment_amount.objects.last().value   
                            dp=driver_payment.objects.filter(user=driver_prof , status=True).first()
                            if dp:
                                driverPayment = True
                                is_paid = True
                    ############# END  driver user   ############### 


                    #####################   start Labour User ########################

                    if labour_contructor.objects.filter(user=userInfo).exists():
                        labourObj=labour_contructor.objects.filter(user=userInfo).first() 
                        if labourObj:
                            labour_id=labourObj.id
                            amount=labour_payment_amount.objects.last().value 
                            Lp=labour_payment.objects.filter(user=labourObj, status=True).first()
                            if Lp:
                                labourPayment = True
                                is_paid = True

                        
                    ################# End Labour User

                    #####################   Start Sub-Contructor User ########################

                    if subcontractorregistration.objects.filter(user=userInfo).exists():

                        subcontructor_prof=subcontractorregistration.objects.filter(user=userInfo).first()

                        if subcontructor_prof:
                            subcontructor_id = subcontructor_prof.id 
                            amount=subcontructor_payment_amount.objects.last().value   
                            dp=subcontructor_payment.objects.filter(user=subcontructor_prof , status=True).first()
                            if dp:
                                subcontructorPayment = True
                                is_paid = True



                    ##### End Sub-Contructor 



                context={
                        "status":True ,
                        "data":{ 
                            "message": "OTP is verified" ,
                            "otp_matched": True ,
                            "is_type": is_type ,
                            "userType":  userType,
                            "is_paid": is_paid ,
                            "vehicle_id": vehicle_id ,
                            
                            ### driver
                            "driver_id": driver_id ,
                            "driverPayment": driverPayment , 

                            ## Labour
                            "labour_id":labour_id ,
                            "labourPayment": labourPayment ,
                            
                            
                            # sub-contrucotr
                            "subcontructor_id" : subcontructor_id ,
                            "subcontructorPayment" : subcontructorPayment,

                            "amount": amount ,
                            "name": name ,


                            "accessToken": get_token.key,
                            "mobileNo":  request.data['mobileNo'] ,
                                }
                    }
                return JsonResponse(context)
            else:
                context={
                            "status":False ,
                            "data":{
                                    "message": "OTP is Invalid" ,
                                    "otp_matched": False ,
                                    "is_type": is_type ,
                                    "userType":  userType,
                                    "is_paid": is_paid ,
                                    "vehicle_id": 0 ,

                                     ### driver
                                    "driver_id": driver_id ,
                                    "driverPayment": driverPayment ,

                                            ## Labour
                                    "labour_id":labour_id ,
                                    "labourPayment": labourPayment ,

                                    # sub-contructor
                                    "subcontructor_id" : 0 ,
                                    "subcontructorPayment" : False ,

                                    "amount": 0 ,
                                    "name": "" ,

                                    "accessToken": "",
                                    "mobileNo":  request.data['mobileNo'] ,
                                    }
                        }
                return JsonResponse(context)

            
        elif(request.data['otp'] == "0000"):
            context={
                    "status":True ,
                    "data":{
                        "message": "OTP is verified" ,
                        "otp_matched": True ,
                        "is_type": True ,
                        "userType":  "",
                        "is_paid": True ,
                        "vehicle_id": 0 ,
                        
                         ### driver
                        "driver_id": driver_id ,
                        "driverPayment": driverPayment ,
                         ## Labour
                        "labour_id":0 ,
                        "labourPayment": False ,
                        # sub-contructor
                        "subcontructor_id" : 0 ,
                        "subcontructorPayment" : False ,    
                        
                        
                        "amount": 0 ,
                        "name": "" ,
                        
                        "accessToken": "",
                        "mobileNo":  "" ,
                            }
                }
            return JsonResponse(context)
            
       
    except Exception as e:
        print('...................verify mobile otp........',str(e))
        context={
                    "status":False ,
                    "data":{
                        "test": request.data["mobileNo"],
                        "message": f"{e}" ,
                        "is_type": False ,
                        "userType":  "",
                        "is_paid": False ,
                        "accessToken": "",
                         ## Labour
                        "labour_id":0 ,
                        "labourPayment": False ,
                        # sub-contructor
                        "subcontructor_id" : 0 ,
                        "subcontructorPayment" : False ,
                        "name": "" ,
                        "mobileNo":  "" ,
                            }
                }
        return JsonResponse(context)

       
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def add_profile(request):
    try:

        get_role = request.data['role']
        
        check_list = ['heavy_vehicle' , 'driver' , 'subcontructor' , 'labour' , 'user']
        if get_role not in  check_list:
            context={
                'status':False,
                'data':{
                    'message': "Plaese select role"
                }
            }
            return JsonResponse(context)
            
        if not profileofall.objects.filter(user=request.user).exists():
            profileofall.objects.create(
            role = get_role ,
            user = request.user 
            )
            if get_role == 'heavy_vehicle':
                vehicle_user_profile.objects.create(user=request.user)
           

        context={
            'status':True,
            'data':{
                'message': "Added Successfully"
            }
        }
        return JsonResponse(context) 
    
    except Exception as e:
        context={
            'status':False,
            'data':{
                'message': f"{e}"
            }
        }
        return JsonResponse(context)
    
class stateListView(generics.ListAPIView):
    serializer_class = stateSerializer
    queryset = state.objects.all()


class districtSerializer(generics.ListAPIView):
    serializer_class = districtSerializer  # Rename the serializer class to DistrictSerializer
    queryset = district.objects.all()

    def list(self, request, *args, **kwargs):
        state_id = self.kwargs['id']
        getstate = get_object_or_404(state, id=state_id)
        districts = district.objects.filter(state_id=getstate.id)
        ser = self.serializer_class(districts, many=True)  # Use self.serializer_class instead of districtSerializer
        return Response(ser.data, status=status.HTTP_200_OK)

class tahseelSerializer(generics. ListAPIView):
    serializer_class = tahseelSerializer  # Rename the serializer class to DistrictSerializer
    queryset = tahseel.objects.all()

    def list(self, request, *args, **kwargs):
        district_id = self.kwargs['id']
        getdistrict = get_object_or_404(district, id=district_id)
        tahseels = tahseel.objects.filter(district_id=getdistrict.id)
        ser = self.serializer_class(tahseels, many=True)  # Use self.serializer_class instead of districtSerializer
        return Response(ser.data, status=status.HTTP_200_OK)


