from all_import.all_import import *





class LabourAddress(serializers.ModelSerializer):
    class Meta:
        model = labour_address
        exclude = ("user", )

class LabourRegistration(serializers.ModelSerializer):
    class Meta:
        model   = labour_contructor
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def labour_registration(request):
    try:
        data = request.data
        serializer = LabourRegistration(data=data)
        if serializer.is_valid():
            serializer.save(user = request.user , is_active=True)
            User.objects.filter(id=request.user.id).update(first_name=data['name'])
            status = True
            msg = "Labour Registerd Succesfully" 
        else:
            status =False 
            msg = f"{serializer.errors}"

        context={
            "status": status ,
            "data": {
                'message': msg ,
                'labour': serializer.data
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
def labouraddress(request):
    try:
        user = labour_contructor.objects.get(user = request.user)
        data = request.data
        serializer = LabourAddress(data=data)
        if serializer.is_valid():
            serializer.save(user = user)
            status = True
            msg = "Labour Address Added Succesfully" 
        else:
            status =False 
            msg = f"{serializer.errors}"

        context={
            "status": status ,
            "data": {
                'message': msg ,
                'labour': serializer.data
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
def labourdashboard(request):
    labour=labour_contructor.objects.get(user=request.user)
    serializer=LabourRegistration(labour,many=False)
    context={
        'status': True ,
        'data':{
            'labour': serializer.data
        }
    }
    return JsonResponse(context)    