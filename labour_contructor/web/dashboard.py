from all_import.all_import import *

@login_required(login_url='account:send-otp')
def labour_dashboard(request):
    dp=labour_contructor.objects.filter(user=request.user , is_active=True).first()
    if not dp:
        messages.success(request , 'You are not allowed here')
        return redirect('account:send-otp')
    
    if not dp.labour_paid:
        if not labour_address.objects.filter(user=dp).exists():
            return redirect('driver:add_driver_address')
        return redirect('driver:driver_making_payment')
                    
    context={
        'labour':dp
    }
    return render(request , 'labour-profile.html' , context)   

@login_required(login_url='account:send-otp')
def labour_view(request,pk):
    try:
        dp=labour_contructor.objects.filter(id=pk , is_active=True).first()
        reh=request_labour.objects.filter(labour_contructor=dp).last()
        context={
            "lab":dp ,
            "reh":reh
        }
        return render(request, 'labour-view.html', context)
    except Exception as e:
        print(e)
        messages.success(request , 'Not Allowed')
        return redirect('account:send-otp')
        
    
