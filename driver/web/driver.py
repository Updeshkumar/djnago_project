from all_import.all_import import *


@login_required(login_url='account:send-otp')
def add_driver_view(request):
    pro_obj = profileofall.objects.filter(user = request.user).first()
    if pro_obj:
        
        if not pro_obj.role == "driver":
            messages.success(request,"You are not allowed here")
            deauth(request)
            return redirect("account:send-otp")
    else:
        return redirect()
    
    if request.method == "POST":
        db = driver_profile.objects.create(
            user = request.user,
            vehicalname=request.POST.get('vehicalname'), 
            expriencesinyear=request.POST.get('expriencesinyear'),
            driveroperatorname=request.POST.get('driveroperatorname'),
            Aadharnumberfrontimage=request.FILES["Aadharnumberfrontimage"],
            Aadharnumberbackimage=request.FILES["Aadharnumberbackimage"],
            alternet_mobilenumber=request.POST.get('alternet_mobilenumber'),
            heavy_license=request.POST.get('heavy_license'),
            emailId=request.POST.get('emailId'),
            mobilenumber=request.POST.get('mobilenumber'),
            license_image=request.FILES['license_image'],
            driver_image=request.FILES["driver_image"] ,
            is_active = True 
              )
        
        User.objects.filter(id=request.user.id).update(first_name =request.POST.get('driveroperatorname'))
        return redirect("driver:add_driver_address")
    
    return render(request, "driver-register.html" , {'no_access':True})

@login_required(login_url='account:send-otp')
def add_driver_address(request):
    user=driver_profile.objects.filter(user=request.user).first()
    if request.POST:
        getstate_id=request.POST.get('state_id')
        getdistrict_id=request.POST.get('district_id')
        gettehsil_id=request.POST.get('tehsil_id')

        print("isd",getdistrict_id,getstate_id,gettehsil_id)
        
        if not getstate_id and getdistrict_id and gettehsil_id:
            messages.success(request , 'All Fields are mandatry')
            return redirect('driver:driveraddress')
        
        driver_Address.objects.create(
            user = user ,
            state_id = state.objects.get(id=getstate_id) ,
            district_id = district.objects.get(id=getdistrict_id) ,
            tahseel_id=tahseel.objects.get(id=gettehsil_id) ,
            is_active=True 
        )  
        messages.success(request, 'Address added successfully')
        return redirect('driver:driver_making_payment')  
        
    states = state.objects.all()
    return render(request,'vehicle-address.html',{'states':states , 'no_access':True})

@login_required(login_url='account:send-otp')
def update_driver_profile(request , pk):
    obj = driver_profile.objects.get(id=pk)
    if request.POST:
        print(request.POST)
        form = AddDriverForm(request.POST , request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            User.objects.filter(id=request.user.id).update(first_name = form.cleaned_data['driveroperatorname'])

            messages.success(request , f'Updated Successfully') 
            return redirect('driver:driver_dashboard')
        else:
            messages.success(request , f"{form.errors}")
            return redirect('driver:update_driver_profile' , pk)    
    
    form = AddDriverForm(instance=obj)
    return render(request , 'driver-update.html' , {'form':form})
