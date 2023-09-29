from all_import.all_import import *


@login_required(login_url='account:send-otp')
def dashboard(request):
    ##Global variable 
    is_vehicle = False 
    is_driver = False
    is_labour = False
    is_sub = False
    is_user = False
    sub_set = []
    drivers=[]
    labours=[]
    vehicles = []
    
    drivers_ids=[]
    sub_set_ids=[]
    labours_ids = []
    vehicles_ids = []

    if profileofall.objects.filter(user=request.user).exists():
        prof=profileofall.objects.filter(user=request.user).first() 
        if prof.role == 'heavy_vehicle':
            is_vehicle = True 
            vup=vehicle_user_profile.objects.filter(user=request.user , is_active=True).first()
            if not vehicle_payment.objects.filter(user=vup , status=True).exists():
                if heavyvehivalregistration.objects.filter(user=vup).exists():
                    hv=heavyvehivalregistration.objects.filter(user=vup).last()
                    if not heavyvehicleaddress.objects.filter(heavyvehivalregistration=hv).exists():
                        return redirect('vehicle_owner:add_heavy_address' ,hv.id )
                    return redirect('vehicle_owner:vehicle_making_payment' , hv.id)
                else:
                    return redirect('vehicle_owner:add_vehicle_view')
        elif prof.role == 'driver':
            is_driver = True
            dp=driver_profile.objects.filter(user=request.user).first()
            if dp:
                if not dp.driver_paid:
                    if not driver_Address.objects.filter(user=dp).exists():
                        return redirect('driver:add_driver_address')
                    else:
                        return redirect('driver:driver_making_payment')
            else:
                return redirect('driver:add_driver_view')
            
        elif prof.role == 'subcontructor':
            is_sub = True 
            dp = subcontractorregistration.objects.filter(user = request.user).first()
            if dp:
                if not dp.subcontructor_paid:
                    if not subcontructor_Address.objects.filter(user=dp).exists():
                        return redirect('sub_contructor: add_subcontructor_address')
                    else:
                        return redirect('sub_contructor: subcontructor_making_payment')
            else:
                return redirect('sub_contructor:add_subcontructor_view')
                
                
        elif prof.role == 'labour':
            is_labour = True
            lc=labour_contructor.objects.filter(user=request.user).first()
            if  lc:
                if not lc.labour_paid:
                    if not labour_address.objects.filter(user=lc).exists():
                        return redirect('labour_contructor:add_labour_address')
                    else:
                        return redirect('labour_contructor:labour_making_payment')    
            else:
                return redirect('labour_contructor:add_labour_view')
        elif prof.role == 'user':
            is_user = True
            nu = user_profile.objects.filter(user = request.user).first()
            if nu:
                if not nu.user_paid:
                    if not user_address.objects.filter(user = nu).exists():
                        return redirect('df_user:add_defaultuser_address')
                    else:
                        return render('df_user: df_user_making_payment')
            else:
                return redirect('df_user:add_defaultuser_view')
        else:
            messages.success(request,'you are not allowed here')
            return redirect('account:send-otp')    
    else:
        return redirect('account:send-otp')



    if request.POST:
        q = request.POST.get('query')
        print(q)
        if not q:
            return redirect('account:home-dashboard')
        
        # vehicle list
        getState=state.objects.filter(state_name__contains=q).first()
        getDistrict=district.objects.filter(district_name__contains=q).first()
        getTehsil = tahseel.objects.filter(tahseel_name__contains=q).first()
        
        print("state", getState)
        print("district" , getDistrict)
        print("Tehisl" , getTehsil)
        
        if getState:
            #vehicle list
            if heavyvehicleaddress.objects.filter(state_id=getState).exists():      
                for i in heavyvehicleaddress.objects.filter(state_id=getState):
                    vehicles_ids.append(i.heavyvehivalregistration.id)
                
                vehicles=heavyvehivalregistration.objects.filter(
                                                                id__in=vehicles_ids,
                                                                is_active=True , 
                                                                is_paid = True , 
                                                                expired_at__gte = date.today(), 
                                                                )
            # driver list                                               
           
            if driver_Address.objects.filter(state_id=getState).exists():      
                for d in driver_Address.objects.filter(state_id=getState):
                    drivers_ids.append(d.user.id)
                
                
                drivers=driver_profile.objects.filter(     id__in=drivers_ids ,
                                                            driver_paid=True ,
                                                            is_active=True ,
                                                            expired_at__gte = date.today() 
                                                            )
            # labour list 
            if labour_address.objects.filter(state_id=getState).exists():
                for l in labour_address.objects.filter(state_id=getState):
                    labours_ids.append(l.user.id)
                
                
                labours=labour_contructor.objects.filter(
                                                    id__in= labours_ids,
                                                    labour_paid=True ,
                                                    is_active=True ,
                                                    expired_at__gte = date.today() )                    
            # sub-contructor list

            if subcontructor_Address.objects.filter(state_id=getState).exists():
                for s in subcontructor_Address.objects.filter(state_id=getState):
                    sub_set_ids.append(s.user.id)

                sub_set=subcontractorregistration.objects.filter(
                                                        id__in=sub_set_ids ,
                                                        subcontructor_paid=True ,
                                                        is_active=True ,
                                                        expired_at__gte = date.today() 
                                                        )
        if getDistrict:
            #vehicle list
            #vehicle list
            if heavyvehicleaddress.objects.filter(district_id=getDistrict).exists():      
                for i in heavyvehicleaddress.objects.filter(district_id=getDistrict):
                    vehicles_ids.append(i.heavyvehivalregistration.id)
                
                vehicles=heavyvehivalregistration.objects.filter(
                                                                id__in=vehicles_ids,
                                                                is_active=True , 
                                                                is_paid = True , 
                                                                expired_at__gte = date.today(), 
                                                                )
            # driver list                                               
           
            if driver_Address.objects.filter(district_id=getDistrict).exists():      
                for d in driver_Address.objects.filter(district_id=getDistrict):
                    drivers_ids.append(d.user.id)
                
                
                drivers=driver_profile.objects.filter(     id__in=drivers_ids ,
                                                            driver_paid=True ,
                                                            is_active=True ,
                                                            expired_at__gte = date.today() 
                                                            )
            # labour list 
            if labour_address.objects.filter(district_id=getDistrict).exists():
                for l in labour_address.objects.filter(district_id=getDistrict):
                    labours_ids.append(l.user.id)
                
                
                labours=labour_contructor.objects.filter(
                                                    id__in= labours_ids,
                                                    labour_paid=True ,
                                                    is_active=True ,
                                                    expired_at__gte = date.today() )                    
            # sub-contructor list

            if subcontructor_Address.objects.filter(district_id=getDistrict).exists():
                for s in subcontructor_Address.objects.filter(district_id=getDistrict):
                    sub_set_ids.append(s.user.id)

                sub_set=subcontractorregistration.objects.filter(
                                                        id__in=sub_set_ids ,
                                                        subcontructor_paid=True ,
                                                        is_active=True ,
                                                        expired_at__gte = date.today() 
                                                        )
        if getTehsil:
            #vehicle list
            if heavyvehicleaddress.objects.filter(tahseel_id=getTehsil).exists():      
                for i in heavyvehicleaddress.objects.filter(tahseel_id=getTehsil):
                    vehicles_ids.append(i.heavyvehivalregistration.id)
                
                vehicles=heavyvehivalregistration.objects.filter(
                                                                id__in=vehicles_ids,
                                                                is_active=True , 
                                                                is_paid = True , 
                                                                expired_at__gte = date.today(), 
                                                                )
            # driver list                                               
           
            if driver_Address.objects.filter(tahseel_id=getTehsil).exists():      
                for d in driver_Address.objects.filter(tahseel_id=getTehsil):
                    drivers_ids.append(d.user.id)
                
                
                drivers=driver_profile.objects.filter(     id__in=drivers_ids ,
                                                            driver_paid=True ,
                                                            is_active=True ,
                                                            expired_at__gte = date.today() 
                                                            )
            # labour list 
            if labour_address.objects.filter(tahseel_id=getTehsil).exists():
                for l in labour_address.objects.filter(tahseel_id=getTehsil):
                    labours_ids.append(l.user.id)
                
                
                labours=labour_contructor.objects.filter(
                                                    id__in= labours_ids,
                                                    labour_paid=True ,
                                                    is_active=True ,
                                                    expired_at__gte = date.today() )                    
            # sub-contructor list

            if subcontructor_Address.objects.filter(tahseel_id=getTehsil).exists():
                for s in subcontructor_Address.objects.filter(tahseel_id=getTehsil):
                    sub_set_ids.append(s.user.id)

                sub_set=subcontractorregistration.objects.filter(
                                                        id__in=sub_set_ids ,
                                                        subcontructor_paid=True ,
                                                        is_active=True ,
                                                        expired_at__gte = date.today() 
                                                        )
        if heavyvehivalregistration.objects.filter( is_active=True , is_paid = True , expired_at__gte = date.today() , vehical_name__contains =  q).exists():
            vehicles = heavyvehivalregistration.objects.filter( is_active=True , is_paid = True , expired_at__gte = date.today() , vehical_name__contains =  q)
            
            
        if driver_profile.objects.filter(is_active = True, driver_paid=True, expired_at__gte = date.today() , vehicalname__contains = q).exists():
            drivers = driver_profile.objects.filter( is_active=True , driver_paid = True , expired_at__gte = date.today() , vehicalname__contains =  q)   

        if subcontractorregistration.objects.filter(is_active = True, subcontructor_paid=True , expired_at__gte = date.today(),typeofwork__contains =  q).exists():                                
            sub_set = subcontractorregistration.objects.filter(is_active=True , subcontructor_paid = True , expired_at__gte = date.today() , typeofwork__contains =  q)
        if labour_contructor.objects.filter(is_active = True, labour_paid = True, expired_at__gte = date.today(),labourwork__contains = q).exists():
            labours = labour_contructor.objects.filter(is_active = True, labour_paid = True, expired_at__gte = date.today(),labourwork__contains = q)

            
                                                            

    else:

        # vehicle list
        vehicles = heavyvehivalregistration.objects.filter( is_active=True , 
                                                            is_paid = True , 
                                                            expired_at__gte = date.today()
                                                        ).order_by("-id")[0:3]
         
        drivers = driver_profile.objects.filter(    
                                                    driver_paid=True ,
                                                    is_active=True ,
                                                    expired_at__gte = date.today()
                                                
                                                ).order_by('-id')[0:3]
        # drivers = driver_profile.objects.filter().first()
        
        # labour list 
        labours = labour_contructor.objects.filter(labour_paid=True ,
                                                is_active=True ,
                                                expired_at__gte = date.today()).order_by('id')[0:3]
        # sub-contructor list
        sub_set = subcontractorregistration.objects.filter(
                                                subcontructor_paid=True ,
                                                is_active=True ,
                                                expired_at__gte = date.today()).order_by('-id')[0:3]
    
    
    context={
        'vehicles':vehicles ,
        'drivers': drivers ,
        'labours': labours ,
        'sub_set': sub_set ,
        'is_vehicle': is_vehicle , 
        'is_driver': is_driver ,
        'is_labour': is_labour ,
        'is_sub': is_sub ,
        'is_user': is_user ,
    }
    
    return render(request , 'dashboard.html' , context)


@login_required(login_url='account:send-otp')
def vehicels_all_view(request):
    vehicles = heavyvehivalregistration.objects.filter(is_active=True , 
                                                    is_paid = True , 
                                                    expired_at__gte = date.today())
    context={
        'vehicles':vehicles
    }
    return render(request, 'view_all/heavy-vehicles.html', context )





@login_required(login_url='account:send-otp')
def drivers_all_view(request):
    drivers = driver_profile.objects.filter(driver_paid=True ,
                                                is_active=True ,
                                            expired_at__gte = date.today())
    context={
        'drivers':drivers
    }
    return render(request, 'view_all/drivers.html' , context)

@login_required(login_url='account:send-otp')
def subcontructor_all_view(request):
    sub_set = subcontractorregistration.objects.filter(
                                            subcontructor_paid=True ,
                                            is_active=True ,
                                            expired_at__gte = date.today())
    context={
        'sub_set':sub_set
    }
    return render(request, 'view_all/subcontructors.html' , context)


@login_required(login_url='account:send-otp')
def labour_all_view(request):
    # labour list 
    labours = labour_contructor.objects.filter(labour_paid=True ,
                                            is_active=True ,
                                            expired_at__gte = date.today())
    context={
        'labours':labours
    }
    return render(request, 'view_all/labours.html' , context)

@login_required(login_url='account:send-otp')
def categories_view(request):
    return render(request , 'categories.html' )




@login_required(login_url='account:send-otp')
def requirement_view(request):
    requiremnts=requirement.objects.filter(is_active=True)
    user=profileofall.objects.filter(user=request.user).first()
    requirements=[]
    for r in requiremnts:
        if accepted_requirement.objects.filter(requirement=r , user=user).exists():
            requirements.append({
                "id": r.id ,
                "title": r.title ,
                "description": r.description ,
                "requirement_image": r.requirement_image.url ,
                "request": True,
                "status": accepted_requirement.objects.get(requirement=r , user=user).status
            })
        else:
            requirements.append({
                 "id": r.id ,
                "title": r.title ,
                "description": r.description ,
                "requirement_image": r.requirement_image.url ,
                "request": False,
                "status": None
            })
    return render(request , 'require.html', {'requirements':requirements})
    
@login_required(login_url='account:send-otp')
def requirement_req_view(request , pk):
    user=profileofall.objects.filter(user=request.user).first()
    accepted_requirement.objects.create(
            user = user ,
            requirement = requirement.objects.get(id=pk) ,
            status = True 
        )
    
    messages.success(request ,"Requested sucessfully ! will contact you soon")
    return redirect('account:requirement_view')

@login_required(login_url='account:send-otp')
def requirement_cancle_view(request , pk):
    user=profileofall.objects.filter(user=request.user).first()
    accepted_requirement.objects.create(
            user = user ,
            requirement = requirement.objects.get(id=pk) ,
            status = False 
        )
    messages.success(request ,"Request Added")
    return redirect('account:requirement_view')