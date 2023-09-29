from all_import.all_import import *





@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def requirement_api(request):
    requiremnts=requirement.objects.filter(is_active=True)
    serializer=RequremntSerializer(requiremnts , many=True )
    
    context={
        'status':True ,
        'data':{
            'message':'requiremnts' ,
            'user': request.user.id ,
            'requiremnts':serializer.data
        }
    }
    return JsonResponse(context)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def requirement_accepted_api(request):
    data=request.data
    user=profileofall.objects.filter(user=request.user).first()
    if accepted_requirement.objects.filter(user=user , requirement__id=data['requirement']):
        return JsonResponse({'status':False , 'data':{'message':"Already Added" , 'obj':{}}})
    
    serializer=AddRequiremnt(data=data)
    if serializer.is_valid():
        serializer.save(user=user)
        status=True
        msg='Added Successfully'
    else:
        status=False
        msg=f'{serializer.errors}'


    context={
        'status':status ,
        'data':{
            'message':msg ,
            'obj':serializer.data
        }
    }
    return JsonResponse(context)