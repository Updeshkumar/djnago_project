from all_import.all_import import *


@login_required(login_url='account:send-otp')
def add_subcontructor_view(request):
    pro_obj = profileofall.objects.filter(user = request.user).first()
    if pro_obj:
        
        if not pro_obj.role == "subcontructor":
            messages.success(request,"You are not allowed here")
            deauth(request)
            return redirect("account:send-otp")
    else:
        return redirect()
    
    if request.method =="POST":
        db = subcontractorregistration.objects.create(
            user = request.user,
            contractorname = request.POST.get('contractorname'),
            firmname = request.POST.get('firmname'),
            typeofwork = request.POST.get('typeofwork'),
            emailId = request.POST.get('emailId'),
            expriencesinyear = request.POST.get('expriencesinyear'),
            license_number = request.POST.get('license_number'),
            Aadharnumberfrontimage = request.FILES['Aadharnumberfrontimage'],
            Aadharnumberbackimage = request.FILES['Aadharnumberbackimage'],
            mobilenumber = request.POST.get('mobilenumber'),
            subcontractor_image = request.FILES['subcontractor_image'],
            subcontractor_image_back = request.FILES['subcontractor_image_back'],
            subcontractor_image_left = request.FILES['subcontractor_image_left'],
            subcontractor_image_right = request.FILES['subcontractor_image_right'],
            is_active = True

        )

        User.objects.filter(id = request.user.id).update(first_name = request.POST.get('contractorname'))
        return redirect('sub_contructor:add_subcontructor_address')
    return render(request, 'subcon_register.html' , {'no_access':True})

            

@login_required(login_url='account:send-otp')
def add_subcontructor_address(request):
    user = subcontractorregistration.objects.filter(user=request.user).first()
    if request.POST:
        getstate_id = request.POST.get('state_id')
        getdistrict_id = request.POST.get('district_id')
        gettehsil_id=request.POST.get('tehsil_id')
        
        if not getstate_id and getdistrict_id and gettehsil_id:
            messages.success(request, 'All Fields are mandatry')
            return redirect(request, 'sub_contructor:add_subcontructor_address')
        subcontructor_Address.objects.create(
            user = user,
            state_id = state.objects.get(id=getstate_id),
            district_id = district.objects.get(id=getdistrict_id),
            tahseel_id = tahseel.objects.get(id=gettehsil_id),
            is_active = True
        )
        messages.success(request, 'Address added successfully')
        return redirect('sub_contructor:subcontructor_making_payment')  
        
    states = state.objects.all()
    return render(request,'vehicle-address.html',{'states':states , 'no_access':True})





@login_required(login_url='account:send-otp')
def update_subcotructor_profile(request , pk):
    obj=subcontractorregistration.objects.get(id=pk)
    if request.POST:
        print(request.POST)
        form = AddSubcontructorForm(request.POST , request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            User.objects.filter(id=request.user.id).update(first_name = form.cleaned_data['contractorname'])

            messages.success(request , f'Updated Successfully') 
            return redirect('sub_contructor:subcontructor_dashboard')
        else:
            messages.success(request , f'{form.errors}') 
            return redirect('sub_contructor:update_subcotructor_profile' , pk) 
                
    form=AddSubcontructorForm(instance=obj)
    return render(request , 'subcontructor-update.html' , {'form':form})



