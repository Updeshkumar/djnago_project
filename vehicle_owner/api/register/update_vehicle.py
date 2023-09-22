from all_import.all_import import *

class HvregisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model   = heavyvehivalregistration
        exclude = ('user',)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def update_vehicle_api(request):
    try:
        get_id = request.data['id']
        obj = heavyvehivalregistration.objects.get(id=get_id)
        serializer=HvregisterationSerializer(obj,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
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