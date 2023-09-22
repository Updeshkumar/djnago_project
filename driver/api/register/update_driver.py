from all_import.all_import import *


class DriverRegistration(serializers.ModelSerializer):
    class Meta:
        model   = driver_profile
        exclude = ('user',)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def driver_update_api(request):
    try:
        
        data = request.data
        obj=driver_profile.objects.get(user=request.user)
        serializer = DriverRegistration(obj , data=data ,partial=True)
        if serializer.is_valid():
            serializer.save()
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

