from all_import.all_import import *


class DriverRequest(serializers.ModelSerializer):
    class Meta:
        model   = request_driver
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def request_driver_api(request):
    user = profileofall.objects.get(user=request.user)
    data = request.data

    # if requested vehicle alreday reserved 
    if request_driver.objects.filter(driver_profile__id=data['driver_profile'] ,
                                       reserved=True).exists():
        context={
            'status': False ,
            'data':
            {
                'message': "This Driver alreday reserved" 
            }
        }
        return JsonResponse(context)
    
    serializer = DriverRequest(data=data)
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

    
    

    
    
    

        





    