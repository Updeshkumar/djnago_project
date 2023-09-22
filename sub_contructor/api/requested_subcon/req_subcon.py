from all_import.all_import import *


class SubcontructorRequest(serializers.ModelSerializer):
    class Meta:
        model   = request_subcontructor
        exclude = ('user',)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def request_subcontructor_api(request):
    user = profileofall.objects.get(user=request.user)
    data = request.data

    # if requested vehicle alreday reserved 
    if request_subcontructor.objects.filter(subcontractorregistration__id=data['subcontractorregistration'] ,
                                       reserved=True).exists():
        context={
            'status': False ,
            'data':
            {
                'message': "This Subcontructor alreday reserved" 
            }
        }
        return JsonResponse(context)
    
    serializer = SubcontructorRequest(data=data)
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

    