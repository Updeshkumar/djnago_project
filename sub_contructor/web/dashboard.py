from all_import.all_import import *

@login_required(login_url='account:send-otp')
def subcontructor_dashboard(request):
    dp=subcontractorregistration.objects.filter(user=request.user , is_active=True).first()
    if not dp:
        messages.success(request , 'You are not allowed here')
        return redirect('account:send-otp')
    
    if not dp.subcontructor_paid:
        if not subcontructor_Address.objects.filter(user=dp).exists():
            return redirect('sub_contructor:add_subcontructor_address')
        return redirect('sub_contructor:subcontructor_making_payment')
                    
    context={
        'subcotructor':dp
    }
    return render(request , 'subcontructor-profile.html' , context)   

@login_required(login_url='account:send-otp')
def subcontructor_view(request,pk):
    # try:
    dp=subcontractorregistration.objects.filter(id=pk , is_active=True).first()
    reh=request_subcontructor.objects.filter(subcontractorregistration=dp).last()
    context={
        "subcon":dp ,
        "reh":reh
    }
    return render(request, 'subcontructor-view.html', context)
    # except Exception as e:
    #     print(e)
    #     messages.success(request , 'Not Allowed')
    #     return redirect('account:send-otp')
        
    
