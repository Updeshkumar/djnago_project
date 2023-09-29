from all_import.all_import import *


# class DrregisterationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model   = driver_profile
#         exclude = ('user',)




class driver_user_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver_Address
        exclude = ("user", )

class DriverRegistration(serializers.ModelSerializer):
    class Meta:
        model   = driver_profile
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def driver_registration(request):
    try:
        
        data = request.data
        serializer = DriverRegistration(data=data)
        if serializer.is_valid():
            serializer.save(user = request.user , is_active=True)
            User.objects.filter(id=request.user.id).update(first_name=data['driveroperatorname'])
            status = True
            msg = "Profile Created Succesfully" 
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
def driveraddress(request):
    try:
        user = driver_profile.objects.get(user = request.user)
        data = request.data
        serializer = driver_user_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user = user)
            status = True
            msg = "driver Address Added Succesfully" 
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
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def driverdashboard(request):
    try:
        driver=driver_profile.objects.get(user=request.user)
        serializer=GETDriver(driver,many=False)
        context={
            'status': True ,
            'data':{
                'driver': serializer.data
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


    
