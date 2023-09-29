from all_import.all_import import *

@login_required(login_url='account:send-otp')
def add_defaultuser_view(request):
    pro_obj = profileofall.objects.filter(user = request.user).first()
    if pro_obj:
        
        if not pro_obj.role == "user":
            messages.success(request,"You are not allowed here")
            deauth(request)
            return redirect("account:send-otp")
    else:
        return redirect()
    
    if request.method =="POST":
        db = user_profile.objects.create(
            user = request.user,
            name = request.POST.get('name'),
            is_active = True

        )

        User.objects.filter(id = request.user.id).update(first_name = request.POST.get('name'))
        return redirect('df_user:add_defaultuser_address')
    return render(request, 'defaultuser_register.html')

            

@login_required(login_url='account:send-otp')
def add_defaultuser_address(request):
    user = user_profile.objects.filter(user=request.user).first()
    if request.POST:
        getstate_id = request.POST.get('state_id')
        getdistrict_id = request.POST.get('district_id')
        gettehsil_id=request.POST.get('tehsil_id')

        if not getstate_id and getdistrict_id and gettehsil_id:
            messages.success(request, 'All Fields are mandatry')
            return redirect(request, 'defaultuser:add_defaultuser_address')
        user_address.objects.create(
            user = user,
            state_id = state.objects.get(id=getstate_id),
            district_id = district.objects.get(id=getdistrict_id),
            tahseel_id = tahseel.objects.get(id=gettehsil_id),
            is_active = True
        )
        messages.success(request, 'Address added successfully')
        return redirect('df_user:df_user_making_payment')  
        
    states = state.objects.all()
    return render(request,'vehicle-address.html',{'states':states})









