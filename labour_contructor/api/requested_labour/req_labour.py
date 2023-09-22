from all_import.all_import import *


class LabourRequest(serializers.ModelSerializer):
    class Meta:
        model   = request_labour
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def request_labour_api(request):
    user = profileofall.objects.get(user=request.user)
    data = request.data

    # if requested vehicle alreday reserved 
    if request_labour.objects.filter(labour_contructor__id=data['labour_contructor'] ,
                                       reserved=True).exists():
        context={
            'status': False ,
            'data':
            {
                'message': "This Labour alreday reserved" 
            }
        }
        return JsonResponse(context)
    
    serializer = LabourRequest(data=data)
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

    
    

    
    
    

        





    