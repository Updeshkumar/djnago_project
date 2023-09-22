from all_import.all_import import *
from account.serializer import *



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def serach_api(request):
    try:
        subList = []
        driver_serializers=[]
        laboursList=[]
        hvlist = []
        
        drivers_ids=[]
        sub_set_ids=[]
        labours_ids = []
        vehicles_ids = []
        data = request.data
        q= data['query']
        
        if not q:
            context = {
            "status": False,
            "data":{
                "message": "data fetched successfuly"  ,
                "user": request.user.id ,
                "vehiclelist": [] ,
                "driver_list": [] , 
                "labour_list": [] ,
                "subcontructor_list":[] ,
                }
            }
            return JsonResponse(context) 
            
        # vehicle list
        getState=state.objects.filter(state_name__contains=q).first()
        getDistrict=district.objects.filter(district_name__contains=q).first()
        getTehsil = tahseel.objects.filter(tahseel_name__contains=q).first()
        
        
        if getState:
            #vehicle list
            if heavyvehicleaddress.objects.filter(state_id=getState).exists():      
                for i in heavyvehicleaddress.objects.filter(state_id=getState):
                    vehicles_ids.append(i.heavyvehivalregistration.id)
                
                vehicles=heavyvehivalregistration.objects.filter(
                                                                id__in=vehicles_ids,
                                                                is_active=True , 
                                                                is_paid = True , 
                                                                expired_at__gte = date.today(), 
                                                                )
                hvlist=AllHeavyVehicle(vehicles , many=True)
                hvlist=hvlist.data
            # driver list                                               
            
            if driver_Address.objects.filter(state_id=getState).exists():      
                for d in driver_Address.objects.filter(state_id=getState):
                    drivers_ids.append(d.user.id)
                
                
                drivers=driver_profile.objects.filter(     id__in=drivers_ids ,
                                                            driver_paid=True ,
                                                            is_active=True ,
                                                            expired_at__gte = date.today() 
                                                            )
                driver_serializers=GETDriver(drivers , many=True)
                driver_serializers=driver_serializers.data
            # labour list 
            if labour_address.objects.filter(state_id=getState).exists():
                for l in labour_address.objects.filter(state_id=getState):
                    labours_ids.append(l.user.id)
                
                
                labours=labour_contructor.objects.filter(
                                                    id__in= labours_ids,
                                                    labour_paid=True ,
                                                    is_active=True ,
                                                    expired_at__gte = date.today() )                    
                laboursList=LabourProfile(labours , many=True)
                laboursList=laboursList.data
            # sub-contructor list

            if subcontructor_Address.objects.filter(state_id=getState).exists():
                for s in subcontructor_Address.objects.filter(state_id=getState):
                    sub_set_ids.append(s.user.id)

                sub_set=subcontractorregistration.objects.filter(
                                                        id__in=sub_set_ids ,
                                                        subcontructor_paid=True ,
                                                        is_active=True ,
                                                        expired_at__gte = date.today() 
                                                        )
                subList = SubContructorProfile(sub_set , many=True)
                subList=subList.data
        
        if getDistrict:
            #vehicle list
            #vehicle list
            if heavyvehicleaddress.objects.filter(district_id=getDistrict).exists():      
                for i in heavyvehicleaddress.objects.filter(district_id=getDistrict):
                    vehicles_ids.append(i.heavyvehivalregistration.id)
                
                vehicles=heavyvehivalregistration.objects.filter(
                                                                id__in=vehicles_ids,
                                                                is_active=True , 
                                                                is_paid = True , 
                                                                expired_at__gte = date.today(), 
                                                                )
                hvlist=AllHeavyVehicle(vehicles , many=True)
                hvlist=hvlist.data
            # driver list                                               
            
            if driver_Address.objects.filter(district_id=getDistrict).exists():      
                for d in driver_Address.objects.filter(district_id=getDistrict):
                    drivers_ids.append(d.user.id)
                
                
                drivers=driver_profile.objects.filter(     id__in=drivers_ids ,
                                                            driver_paid=True ,
                                                            is_active=True ,
                                                            expired_at__gte = date.today() 
                                                            )
                driver_serializers=GETDriver(drivers , many=True)
                driver_serializers=driver_serializers.data
            # labour list 
            if labour_address.objects.filter(district_id=getDistrict).exists():
                for l in labour_address.objects.filter(district_id=getDistrict):
                    labours_ids.append(l.user.id)
                
                
                labours=labour_contructor.objects.filter(
                                                    id__in= labours_ids,
                                                    labour_paid=True ,
                                                    is_active=True ,
                                                    expired_at__gte = date.today() )   
                laboursList=LabourProfile(labours , many=True)       
                laboursList=laboursList.data          
            # sub-contructor list

            if subcontructor_Address.objects.filter(district_id=getDistrict).exists():
                for s in subcontructor_Address.objects.filter(district_id=getDistrict):
                    sub_set_ids.append(s.user.id)

                sub_set=subcontractorregistration.objects.filter(
                                                        id__in=sub_set_ids ,
                                                        subcontructor_paid=True ,
                                                        is_active=True ,
                                                        expired_at__gte = date.today() 
                                                        )
                subList = SubContructorProfile(sub_set , many=True)
                subList=subList.data
        if getTehsil:
            #vehicle list
            if heavyvehicleaddress.objects.filter(tahseel_id=getTehsil).exists():      
                for i in heavyvehicleaddress.objects.filter(tahseel_id=getTehsil):
                    vehicles_ids.append(i.heavyvehivalregistration.id)
                
                vehicles=heavyvehivalregistration.objects.filter(
                                                                id__in=vehicles_ids,
                                                                is_active=True , 
                                                                is_paid = True , 
                                                                expired_at__gte = date.today(), 
                                                                )
                hvlist=AllHeavyVehicle(vehicles , many=True)
                hvlist=hvlist.data
            # driver list                                               
            
            if driver_Address.objects.filter(tahseel_id=getTehsil).exists():      
                for d in driver_Address.objects.filter(tahseel_id=getTehsil):
                    drivers_ids.append(d.user.id)
                
                
                drivers=driver_profile.objects.filter(     id__in=drivers_ids ,
                                                            driver_paid=True ,
                                                            is_active=True ,
                                                            expired_at__gte = date.today() 
                                                            )
                driver_serializers=GETDriver(drivers , many=True)
                driver_serializers=driver_serializers.data
            # labour list 
            if labour_address.objects.filter(tahseel_id=getTehsil).exists():
                for l in labour_address.objects.filter(tahseel_id=getTehsil):
                    labours_ids.append(l.user.id)
                
                
                labours=labour_contructor.objects.filter(
                                                    id__in= labours_ids,
                                                    labour_paid=True ,
                                                    is_active=True ,
                                                    expired_at__gte = date.today() ) 
                laboursList=LabourProfile(labours , many=True)  
                laboursList=laboursList.data                 
            # sub-contructor list

            if subcontructor_Address.objects.filter(tahseel_id=getTehsil).exists():
                for s in subcontructor_Address.objects.filter(tahseel_id=getTehsil):
                    sub_set_ids.append(s.user.id)

                sub_set=subcontractorregistration.objects.filter(
                                                        id__in=sub_set_ids ,
                                                        subcontructor_paid=True ,
                                                        is_active=True ,
                                                        expired_at__gte = date.today() 
                                                        )
                subList = SubContructorProfile(sub_set , many=True)
                subList=subList.data
                
        context = {
            "status": True,
            "data":{
                "message": "data fetched successfuly"  ,
                "user": request.user.id ,
                "vehiclelist": hvlist ,
                "driver_list": driver_serializers , 
                "labour_list": laboursList ,
                "subcontructor_list": subList ,
            }
        }
        return JsonResponse(context)     
    except Exception as e:
        context = {
            "status": False,
            "data":{
                "message": f"{e}"  ,
                "user": request.user.id ,
                "vehiclelist": [] ,
                "driver_list": [] , 
                "labour_list": [] ,
                "subcontructor_list":[] ,
                }
            }
        return JsonResponse(context) 

