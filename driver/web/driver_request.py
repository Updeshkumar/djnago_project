from all_import.all_import import *

@login_required(login_url='account:send-otp')
def driver_request_view(request , pk):
    prof = profileofall.objects.get(user=request.user)

   
    dp=driver_profile.objects.filter(id=pk).first()
    
    
    # if requested vehicle alreday reserved 
    if request_driver.objects.filter(driver_profile=dp ,
                                       reserved=True).exists():
        messages.success(request , "This Vehicle Already Reserved by someone else ")
       
    else:
        request_driver.objects.create(
            user = prof ,
            driver_profile = dp ,
            reserved = False
        )

        messages.success(request , 'Requested Successfully')
    
    
    return redirect('driver:driver_view' , pk)
    
