from all_import.all_import import *

class defaultuser_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_address
        exclude = ("user",)


class defaultuser(serializers.ModelSerializer):
    class Meta:
        model = user_profile
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def defaultuser_registration(request):
    try:
        
        data = request.data
        serializer = defaultuser(data=data)
        if serializer.is_valid():
            serializer.save(user = request.user , is_active=True)
            User.objects.filter(id=request.user.id).update(first_name=data['name'])
            status = True
            msg = "Profile Created Succesfully" 
        else:
            status =False 
            msg = f"{serializer.errors}"

        context={
            "status": status ,
            "data": {
                'message': msg ,
                'subcontructor': serializer.data
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
def defaultuser_Address(request):
    try:
        user = user_profile.objects.get(user = request.user)
        data = request.data
        serializer = defaultuser_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user = user , is_active=True)

            status = True
            msg = "Normaluser Address Added Succesfully" 
        else:
            status =False 
            msg = f"{serializer.errors}"

        context={
            "status": status ,
            "data": {
                'message': msg ,
                'defaultuser': serializer.data
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
def defaultuserdashboard(request):
    obj=user_profile.objects.get(user=request.user)
    serializer=defaultuser_dataSerializer(obj,many=False)
    context={
        'status': True ,
        'data':{
            'driver': serializer.data
        }
    }
    return JsonResponse(context)
