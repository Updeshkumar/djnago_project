from all_import.all_import import *



def add_vehicle_view(request):
    pro_obj = profileofall.objects.filter(user = request.user).first()
    if pro_obj:
        
        if not pro_obj.role == "heavy_vehicle":
            messages.success(request,"You are not allowed here")
            deauth(request)
            return redirect("account:send-otp")
    else:
        return redirect()
    
    no_access=True
    user = vehicle_user_profile.objects.get(user=request.user)
    
    if request.method == "POST":
        
        db = heavyvehivalregistration.objects.create(
            user = user,
            vehical_name = request.POST.get('vehical_name'), 
            company_name=request.POST.get("company_name"),
            emailId=request.POST.get('emailId'),
            ownername=request.POST.get('ownername'),
            vehicleregistrationnumber=request.POST.get('vehicleregistrationnumber'),
            Aadharnumberfrontimage=request.FILES["Aadharnumberfrontimage"],
            Aadharnumberbackimage=request.FILES["Aadharnumberbackimage"],
            vehicle_image=request.FILES["vehicle_image"],
            vehicle_image_back=request.FILES["vehicle_image_back"],
            vehicle_image_left=request.FILES["vehicle_image_left"],
            vehicle_image_right=request.FILES["vehicle_image_right"], 
            manufacture_date=request.POST.get('manufacture_date'),
            alternativemobilenumber=request.POST.get('alternativemobilenumber'),
            vehiclemodelnumber=request.POST.get('vehiclemodelnumber'),
            is_active = True 
              )
        
        User.objects.filter(id=request.user.id).update(first_name = request.POST.get('ownername'))
        return redirect("vehicle_owner:add_heavy_address", db.id)
    
    if heavyvehivalregistration.objects.filter(user=user ,is_paid=True):
        no_access=False

    return render(request, "add_heavy_vehicle.html", {'no_access':no_access})


def add_heavy_address(request , pk):
    user=vehicle_user_profile.objects.filter(user=request.user).first()
    no_access=True
    if request.POST:
        getstate_id=request.POST.get('state_id')
        getdistrict_id=request.POST.get('district_id')
        gettehsil_id=request.POST.get('tehsil_id')

        print("isd",getdistrict_id,getstate_id,gettehsil_id)
        
        if not getstate_id and getdistrict_id and gettehsil_id:
            messages.success(request , 'All Fields are mandatry')
            return redirect('vehicle_owner:add_heavy_address',pk)
        
        heavyvehicleaddress.objects.create(
            user = user ,
            heavyvehivalregistration = heavyvehivalregistration.objects.get(id=pk),
            state_id = state.objects.get(id=getstate_id) ,
            district_id = district.objects.get(id=getdistrict_id) ,
            tahseel_id=tahseel.objects.get(id=gettehsil_id) 
        )    
        messages.success(request ,'Address Added Successfully')
        return redirect('vehicle_owner:vehicle_making_payment' , pk)
    
    if heavyvehivalregistration.objects.filter(user=user ,is_paid=True):
        no_access=False
    
    
    states = state.objects.all()
    return render(request,'vehicle-address.html',{'states':states , 'no_access':no_access})

def get_districts(request):
    state_id=request.GET.get('state_id')
    districts=district.objects.filter(state_id=state_id)
    return render(request , 'partials/districts.html',{'districts':districts})

def get_tehsils(request):
    district_id=request.GET.get('district_id')
    tehsils=tahseel.objects.filter(district_id=district_id)
    return render(request , 'partials/tehseel.html',{'tehsils':tehsils})



def update_vehicle(request , pk):
    obj=heavyvehivalregistration.objects.get(id=pk)
    if request.POST:
        print(request.POST)
        form = AddHeavyVehile(request.POST , request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request , f'Updated Successfully') 
            return redirect('vehicle_owner:vehicle_dashboard')
        else:
            messages.success(request , f'{form.errors}') 
            return redirect('vehicle_owner:update_vehicle' , pk) 
                
    form=AddHeavyVehile(instance=obj)
    return render(request , 'vehicle-update.html'  , {'form':form})



