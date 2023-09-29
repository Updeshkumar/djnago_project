from all_import.all_import import *
from account.serializer import *



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def home_api(request):
    # try:
    # vehicles = heavyvehivalregistration.objects.filter(is_active=True , 
    #                                                 is_paid = True , 
    #                                                 expired_at__gte = date.today())
    vehicles = heavyvehivalregistration.objects.all()
    
    
    hvlist=AllHeavyVehicle(vehicles , many=True)


    # driver list
    # drivers=driver_profile.objects.filter(driver_paid=True ,
    #                                         is_active=True ,
    #                                     expired_at__gte = date.today())
    drivers=driver_profile.objects.all()
    
    driver_serializers=GETDriver(drivers , many=True)

    # labour list 
    # labours = labour_contructor.objects.filter(labour_paid=True ,
    #                                         is_active=True ,
    #                                     expired_at__gte = date.today())
    labours = labour_contructor.objects.all()
    laboursList=LabourProfile(labours , many=True)

    # sub-contructor list
    # sub_set=subcontractorregistration.objects.filter(
    #                                         subcontructor_paid=True ,
    #                                         is_active=True ,
    #                                     expired_at__gte = date.today())
    sub_set=subcontractorregistration.objects.all()
    subList = SubContructorProfile(sub_set , many=True)

    
    context = {
        "status": True,
        "data":{
            "message": "data fetched successfuly"  ,
            "user": request.user.id ,
            "vehiclelist": hvlist.data ,
            "driver_list": driver_serializers.data , 
            "labour_list": laboursList.data ,
            "subcontructor_list": subList.data ,
        }
    }
    return JsonResponse(context)

        
    # except Exception as e:
    #     context = {
    #         "status": False ,
    #         "data":{
    #             "message": f"{e}"  ,
    #             "vehiclelist": [] ,
    #             "driver_list": [] ,
    #             "labour_list": [] ,
    #             "subcontructor_list":[]
    #         }
    #     }
    #     return JsonResponse(context) 
    
