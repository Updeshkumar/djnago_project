from all_import.all_import import *


class VehicleRequest(serializers.ModelSerializer):
    class Meta:
        model   = request_vehicle
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def request_vehicle_api(request):
    user = profileofall.objects.get(user=request.user)
    data = request.data

    # if requested vehicle alreday reserved 
    if request_vehicle.objects.filter(heavyvehivalregistration__id=data['heavyvehivalregistration'] ,
                                       reserved=True).exists():
        context={
            'status': False ,
            'data':
            {
                'message': "This vehicle alreday reserved" 
            }
        }
        return JsonResponse(context)
    
    serializer = VehicleRequest(data=data)
    if serializer.is_valid():
        serializer.save(user=user)
        status = True
        msg = 'Requested Successfully'
    else:
        status = False
        msg = f'{serializer.errors}'

    
    context={
        'status': status ,
        'data': {
            'message': msg 
        }
    }
    return JsonResponse(context)    

    
    

    
    
    

        





    