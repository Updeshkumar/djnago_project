from all_import.all_import import *

@login_required(login_url='account:send-otp')
def driver_dashboard(request):
    dp=driver_profile.objects.filter(user=request.user , is_active=True).first()
    if not dp:
        messages.success(request , 'You are not allowed here')
        return redirect('account:send-otp')
    
    if not dp.driver_paid:
        if not driver_Address.objects.filter(user=dp).exists():
            return redirect('driver:add_driver_address')
        return redirect('driver:driver_making_payment')
                    
    context={
        'driver':dp
    }
    return render(request , 'driver-profile.html' , context)   

@login_required(login_url='account:send-otp')
def driver_view(request,pk):
    try:
        dp=driver_profile.objects.filter(id=pk , is_active=True).first()
        reh=request_driver.objects.filter(driver_profile=dp).last()
        context={
            "dr":dp ,
            "reh":reh
        }
        return render(request, 'driver-view.html', context)
    except Exception as e:
        print(e)
        messages.success(request , 'Not Allowed')
        return redirect('account:send-otp')
        
    
