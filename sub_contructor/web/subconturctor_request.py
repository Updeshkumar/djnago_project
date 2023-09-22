from all_import.all_import import *


@login_required(login_url='account:send-otp')
def request_subcontructor_view(request , pk):
    prof = profileofall.objects.get(user=request.user)

   
    dp=subcontractorregistration.objects.filter(id=pk).first()
    
    
    # if requested Subcontructor alreday reserved 
    if request_subcontructor.objects.filter(subcontractorregistration=dp ,
                                       reserved=True).exists():
        messages.success(request , "This Subcontructor Already Reserved by someone else ")
       
    else:
        request_subcontructor.objects.create(
            user = prof ,
            subcontractorregistration = dp ,
            reserved = False
        )

        messages.success(request , 'Requested Successfully')
    
    
    return redirect('sub_contructor:subcontructor_view' , pk)