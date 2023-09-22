from all_import.all_import import *

class subcontructor_user_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = subcontructor_Address
        exclude = ("user",)


class subcontructor(serializers.ModelSerializer):
    class Meta:
        model = subcontractorregistration
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def subcontructor_registration(request):
    try:
        
        data = request.data
        serializer = subcontructor(data=data)
        if serializer.is_valid():
            serializer.save(user = request.user , is_active=True)
            User.objects.filter(id=request.user.id).update(first_name=data['contractorname'])
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
def subcontructor_Address(request):
    try:
        user = subcontractorregistration.objects.get(user = request.user)
        data = request.data
        serializer = subcontructor_user_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user = user , is_active=True)

            status = True
            msg = "Subcontructor Address Added Succesfully" 
        else:
            status =False 
            msg = f"{serializer.errors}"

        context={
            "status": status ,
            "data": {
                'message': msg ,
                'Subcontructor': serializer.data
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
def subcontructordashboard(request):
    obj=subcontractorregistration.objects.get(user=request.user)
    serializer=SubContructorProfile(obj,many=False)
    context={
        'status': True ,
        'data':{
            'subcontructor': serializer.data
        }
    }
    return JsonResponse(context)
