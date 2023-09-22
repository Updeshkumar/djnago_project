from all_import.all_import import *




def vehicle_request_view(request , pk):
    prof = profileofall.objects.get(user=request.user)

   
    hv=heavyvehivalregistration.objects.filter(id=pk).first()
    
    
    # if requested vehicle alreday reserved 
    if request_vehicle.objects.filter(heavyvehivalregistration=hv ,
                                       reserved=True).exists():
        messages.success(request , "This Vehicle Already Reserved by someone else ")
       
    else:
        request_vehicle.objects.create(
            user = prof ,
            heavyvehivalregistration = hv ,
            reserved = False
        )

        messages.success(request , 'Requested Successfully')
    
    
    
    return redirect('vehicle_owner:vehicle_view' , pk)
    
    
    
    
    
