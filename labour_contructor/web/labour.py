from all_import.all_import import *


@login_required(login_url='account:send-otp')
def add_labour_view(request):
    pro_obj = profileofall.objects.filter(user = request.user).first()
    if pro_obj:
        
        if not pro_obj.role == "labour":
            messages.success(request,"You are not allowed here")
            deauth(request)
            return redirect("account:send-otp")
    else:
        return redirect("/")
    
    if request.method == "POST":
        form = AddLabourForm(request.POST , request.FILES)
        if form.is_valid():
            new=form.save(commit=False)
            new.user=request.user
            new.is_active=True
            new.save()
            User.objects.filter(id=request.user.id).update(first_name =request.POST.get('name'))
            return redirect("labour_contructor:add_labour_address")
        else:
            messages.success(request , f'{form.errors}')
            return redirect('labour_contructor:add_labour_view')
    
    return render(request, "labour-register.html" , {'no_access':True})


@login_required(login_url='account:send-otp')
def update_labour_profile(request , pk):
    obj=labour_contructor.objects.get(id=pk)
    if request.POST:
        print(request.POST)
        form = AddLabourForm(request.POST , request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request , f'Updated Successfully') 
            return redirect('labour_contructor:labour_dashboard')
        else:
            messages.success(request , f'{form.errors}') 
            return redirect('labour_contructor:update_labour_profile' , pk) 
                
    form=AddLabourForm(instance=obj)
    return render(request , 'labour-contructor-update.html' , {'form':form})




@login_required(login_url='account:send-otp')
def add_labour_address(request):
    user=labour_contructor.objects.filter(user=request.user).first()
    if request.POST:
        getstate_id=request.POST.get('state_id')
        getdistrict_id=request.POST.get('district_id')
        gettehsil_id=request.POST.get('tehsil_id')

        print("isd",getdistrict_id,getstate_id,gettehsil_id)
        
        if not getstate_id and getdistrict_id and gettehsil_id:
            messages.success(request , 'All Fields are mandatry')
            return redirect('labour_contructor:add_labour_address')
        
        labour_address.objects.create(
            user = user ,
            state_id = state.objects.get(id=getstate_id) ,
            district_id = district.objects.get(id=getdistrict_id) ,
            tahseel_id=tahseel.objects.get(id=gettehsil_id) ,
            is_active=True 
        )  
        messages.success(request, 'Address added successfully')
        return redirect('labour_contructor:labour_making_payment')  
        
    states = state.objects.all()
    return render(request,'vehicle-address.html',{'states':states , 'no_access':True})

