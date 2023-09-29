from all_import.all_import import *


def vehicle_dashboard(request):
    vup=vehicle_user_profile.objects.filter(user=request.user , is_active=True).first()
    if not vup:
        messages.success(request , 'You are not allowed here')
        return redirect('account:send-otp')
    


    if not vehicle_payment.objects.filter(user=vup , status=True).exists():
        if heavyvehivalregistration.objects.filter(user=vup).exists():
            hv=heavyvehivalregistration.objects.filter(user=vup).last()
            if not heavyvehicleaddress.objects.filter(heavyvehivalregistration=hv).exists():
                return redirect('vehicle_owner:add_heavy_address' ,hv.id )
            return redirect('vehicle_owner:vehicle_making_payment' , hv.id)
        else:
            return redirect('vehicle_owner:add_vehicle_view')

    getProfile = profileofall.objects.filter(user=request.user).first()    
        
    heavy_vehicl = heavyvehivalregistration.objects.filter(user=vup)
    requestedVcs = request_vehicle.objects.filter(user=getProfile , reserved=True)
    requestedLbs = request_labour.objects.filter(user=getProfile , reserved=True)
    requestedSub = request_subcontructor.objects.filter(user=getProfile , reserved=True)
    requestedDrs = request_driver.objects.filter(user=getProfile , reserved=True)
    
    
    context={
        'vehicles'     : heavy_vehicl,
        'requestedVcs' : requestedVcs ,
        'requestedLbs' : requestedLbs ,
        'requestedSub' : requestedSub ,
        'requestedDrs' : requestedDrs ,
    }
    print(context)
    return render(request , 'vehicle-dashboard.html' , context)   


def vehicle_view(request,pk):
    try:
        hv = heavyvehivalregistration.objects.filter(id=pk).first()
        reh=request_vehicle.objects.filter(heavyvehivalregistration=hv).last()
        context={
            "hv": hv,
            "reh":reh
        }
        return render(request, 'vehicle-detail.html', context)
    except Exception as e:
        print('exception',e)
        messages.success(request , 'Not Allowed')
        return redirect('account:send-otp')
        
    
