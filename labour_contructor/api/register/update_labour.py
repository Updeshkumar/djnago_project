from all_import.all_import import *


class LabourRegistration(serializers.ModelSerializer):
    class Meta:
        model   = labour_contructor
        exclude = ('user',)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def labour_update_api(request):
    try:
        
        data = request.data
        obj=labour_contructor.objects.get(user=request.user)
        serializer = LabourRegistration(obj , data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
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

