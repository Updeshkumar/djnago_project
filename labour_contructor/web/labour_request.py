from all_import.all_import import *


@login_required(login_url='account:send-otp')
def labour_request_view(request,pk):
    prof = profileofall.objects.get(user=request.user)

   
    dp=labour_contructor.objects.filter(id=pk).first()
    
    
    # if requested vehicle alreday reserved 
    if request_labour.objects.filter(labour_contructor=dp ,
                                       reserved=True).exists():
        messages.success(request , "This Labour Contructor Already Reserved by someone else ")
       
    else:
        request_labour.objects.create(
            user = prof ,
            labour_contructor = dp ,
            reserved = False
        )

        messages.success(request , 'Requested Successfully')
    
    
    return redirect('labour_contructor:labour_view' , pk)