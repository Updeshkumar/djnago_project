from all_import.all_import import *


class HvregisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model   = heavyvehivalregistration
        exclude = ('user',)

class address_user_dataSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = heavyvehicleaddress
        exclude = ("user", )


class dataSerializer(serializers.ModelSerializer):
    state_id = serializers.ReadOnlyField(source='state_id.state_name')
    district_id = serializers.ReadOnlyField(source='district_id.district_name')
    tahseel_id = serializers.ReadOnlyField(source='tahseel_id.tahseel_name')

    class Meta:
        model = heavyvehicleaddress
        fields = (
            "state_id" ,
            "district_id" ,
            "tahseel_id"
        )	


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def hvregistration(request):
    try:
        get_profile = vehicle_user_profile.objects.get(user=request.user)
        data = request.data
        serializer=HvregisterationSerializer(data=data) 
        
        if heavyvehivalregistration.objects.filter(
            vehicleregistrationnumber=data['vehicleregistrationnumber']).exists():
            status = False 
            msg = "This vehicle already registerd by someone else"
            obj = {}

        else:    

            if serializer.is_valid():
                serializer.save(user=get_profile, is_active = True)
                User.objects.filter(id=request.user.id).update(first_name=data['ownername'])
                status = True
                msg = "Vehicle added successfully"
                obj=serializer.data
            else:
                status = False
                msg = f"{serializer.errors}"
                obj = {}

        context={
            'status':status,
            'data':{
                'message': msg ,
                'obj': obj 
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
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def hvaddress(request):
    try:
        user = vehicle_user_profile.objects.get(user=request.user)
        data = request.data
        serializer = address_user_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user = user, is_active = True)
            status = True
            msg = "Adress Added Succesfully" 
        else:
            status =False 
            msg = f"{serializer.errors}"

        context={
            "status": status ,
            "data": {
                'message': msg ,
                'vehicle': serializer.data
            }

        }
        return JsonResponse(context)
    except Exception as e:
        context={
            "status": False ,
            "data": {
                'message': f"{e}"
            }

        }
        return JsonResponse(context)

    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def vehicle_user_data(request):
    try:
        user = vehicle_user_profile.objects.get(user=request.user)
        objs = heavyvehivalregistration.objects.filter(user = user)
        hvlist = []

        for i in objs:
            
            # Fetching Address
            obj_addr = heavyvehicleaddress.objects.filter(user = user, heavyvehivalregistration = i).last()
            hv = dataSerializer(obj_addr, many=False)
            # Fethcing Payment Details
            v_pay=vehicle_payment.objects.filter(user=user ,status=True ,heavyvehivalregistration=i).last()
            is_paid = True if v_pay else False  
            # Fetching Vehicle requested detils
            reqhv = request_vehicle.objects.filter(heavyvehivalregistration = i ,reserved=True ).last()
            is_reserved = True if reqhv else False
                
            dt = {
                "id": i.id,
                "user": i.user.user.first_name,
                "vehical_name": i.vehical_name,
                "company_name": i.company_name,
                "emailId": i.emailId,
                "ownername": i.ownername,
                "vehicleregistrationnumber": i.vehicleregistrationnumber,
                "Aadharnumberfrontimage": i.Aadharnumberfrontimage.url,
                "Aadharnumberbackimage": i.Aadharnumberbackimage.url,
                "vehicle_image": i.vehicle_image.url,
                "vehicle_image_back": i.vehicle_image_back.url,
                "vehicle_image_left": i.vehicle_image_left.url,
                "vehicle_image_right": i.vehicle_image_right.url,
                "manufacture_date" : i.manufacture_date,
                "alternativemobilenumber" : i.alternativemobilenumber,
                "vehiclemodelnumber": i.vehiclemodelnumber,
                "is_active": i.is_active  , 
                "expired_at": i . expired_at ,
                "is_reserved": is_reserved,
                "is_paid": is_paid , 
                "amount": vehicle_payment_amount.objects.last().value ,
                "address": hv.data 
            }
            hvlist.append(dt)

        context = {
            "status": True,
            "data":{
                "message": "data fetched successfuly"  ,
                "vehiclelist": hvlist 
            }
        }
        return JsonResponse(context)

        
    except Exception as e:
        context = {
            "status": False ,
            "data":{
                "message": f"{e}"  ,
                "vehiclelist": [] 
            }
        }
        return JsonResponse(context) 
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def address_user_data(request):
    user = vehicle_user_profile.objects.get(user=request.user)
    obj = heavyvehicleaddress.objects.filter(user = user)
    serializers = address_user_dataSerializer(obj, many=True)
    return JsonResponse(serializers.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def letest_vehicle_data(request):
    user = vehicle_user_profile.objects.get(user=request.user)
    dashboard_access = False
    if vehicle_payment.objects.filter(user=user , status=True).exists():
        dashboard_access = True 

    vehicle_id - 0
    hv_obj = heavyvehivalregistration.objects.filter(user = user).last()
    if hv_obj:
        vehicle_id = hv_obj.id


    getaddress=heavyvehicleaddress.objects.filter(heavyvehivalregistration=hv_obj , user=user)
    getpayment= vehicle_payment.objects.filter(user=user , heavyvehivalregistration=hv_obj , status=True)
    
    
    if getpayment:
        payment_completed = True
    else:
        payment_completed = False    
    
    if getaddress:
        address_completed = True 
    else:
        address_completed = False    



    context = {
        'status': True ,
        'data':{
            'message': "Vehicle fetched Successfully",
            'vehicle_id': vehicle_id,
            'address_completed':  address_completed ,
            'payment_completed': payment_completed ,
            'dashboard_access': dashboard_access 
        }
    }
    return JsonResponse(context)    
        
        
    
        
