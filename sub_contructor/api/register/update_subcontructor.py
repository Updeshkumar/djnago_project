from all_import.all_import import *


class SubcontructorRegistration(serializers.ModelSerializer):
    class Meta:
        model   = subcontractorregistration
        exclude = ('user',)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def subcontructor_update_api(request):
    try:
        
        data = request.data
        obj=subcontractorregistration.objects.get(user=request.user)
        serializer = SubcontructorRegistration(obj , data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
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

