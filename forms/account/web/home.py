from all_import.all_import import *


def send_otp(mobileNo,otpToSave):
    url = f"https://control.msg91.com/api/v5/otp?template_id=64ae465ed6fc050316082ec3&mobile=91{mobileNo}"

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authkey": "399430AXHWNUNwrm64ae44f2P1"
    }

    response = requests.post(url, headers=headers)
    print(response.text)
    
def chooselanguage(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin')
        get_prof= profileofall.objects.filter(user=request.user).first()
        if get_prof:
            return redirect('account:home-dashboard')
        else:
            return redirect('account:choose-profile') 
    return render(request, "chooselanguage.html")


def dumydashboard(request):
    return render(request, 'dummydashboard.html')




def sendotp(request):
    
    if request.user.is_authenticated:
        print("You was authenticated")
        deauth(request)

    if request.method=="POST":
       
        mobileNo = request.POST['mobileNo']

        if not mobileNo:
            messages.success(request , "Please Enter  Phone Number")
            return redirect('account:send-otp')
        
        if not len(mobileNo) == 10:
            messages.success(request , "Please enter 10 Digit Phone Number")
            return redirect('account:send-otp')
        
        otp=str(random.randint(1000 , 9999)) 
        request.session['mobileNo']=mobileNo  
        print("Your Otp is", otp) 
        print("saveUser=",User.objects.filter(mobile_number=mobileNo))
        if not User.objects.filter(mobile_number=mobileNo).exists():
            saveUser = User(mobile_number = mobileNo)
            saveUser.save()
            saveUser.set_password(mobileNo)
            saveUser.save()

            User.objects.filter(mobile_number=mobileNo).update(otp=otp)
            send_otp(mobileNo, otp)
            message = str(otp)+" is your verification code for AHV App."
            
            return redirect('account:verify-otp')
        else: 
            User.objects.filter(mobile_number=mobileNo).update(otp=otp)
            send_otp(mobileNo, otp)

            return redirect('account:verify-otp')
          
    return render(request, 'send-otp.html')



def msgverifyotp(mobile, otp):
    url = f"https://control.msg91.com/api/v5/otp/verify?otp={otp}&mobile=91{mobile}"

    headers = {
        "accept": "application/json",
        "authkey": "399430AXHWNUNwrm64ae44f2P1"
    }

    response = requests.get(url, headers=headers)

    return response.text

import ast
def verify_otp(request):


    ### GLOBAL VARIABLES
    is_type = False
    userType = ""
   

    getMob=request.session.get('mobileNo')
    if request.POST:
        mobilNo = request.POST.get('mobileNo')
        otp = request.POST.get('otp')

        if not otp :
            messages.success(request , 'Please enter otp')
            return redirect('account:verify-otp')
        
        msgcheckotp = msgverifyotp(mobilNo,int(otp))

        print('mydict',msgcheckotp)
        # {"request_id":"336771704e72353839373836","type":"success"}
        res = ast.literal_eval(msgcheckotp)
        if res["type"] == "success":
        
            messages.success(request , 'Good to go')

            userInfo = User.objects.filter(mobile_number=mobilNo).first()
            print(userInfo)

            if not userInfo.active:
                messages.success(request , 'You are not allowed Here!!')
                return redirect('account:verify-otp')

            
            my_user=authenticate(request,mobile_number=mobilNo , password=mobilNo)
            print("user is ",my_user)
            login(request ,my_user )
            
                      
            if profileofall.objects.filter(user=userInfo).exists(): 
                userType = profileofall.objects.filter(user=userInfo).first().role
                if userType == 'heavy_vehicle':
                    
                    ### HEAVY VEHICLE USER
                    vup=vehicle_user_profile.objects.filter(user=userInfo).first()

                    if vehicle_payment.objects.filter(user=vup , status=True).exists():
                        return redirect('account:home-dashboard')
                    else:
                        if heavyvehivalregistration.objects.filter(user=vup).exists():
                            hv=heavyvehivalregistration.objects.filter(user=vup).last()
                            if not heavyvehicleaddress.objects.filter(heavyvehivalregistration=hv).exists():
                                return redirect('vehicle_owner:add_heavy_address' ,hv.id )
                            return redirect('vehicle_owner:vehicle_making_payment' , hv.id)
                        
                        else:
                            return redirect('vehicle_owner:add_vehicle_view')
                ### DRIVER USER
                elif userType == 'driver':
                    dp=driver_profile.objects.filter(user=userInfo).first()
                    if  dp:
                        if not dp.driver_paid:
                            if not driver_Address.objects.filter(user=dp).exists():
                                return redirect('driver:add_driver_address')
                            return redirect('driver:driver_making_payment')
                        return redirect('account:home-dashboard')    
                    return redirect('driver:add_driver_view')
                            
                ### Subcontructor User
                elif userType == "subcontructor":
                    dp = subcontractorregistration.objects.filter(user=userInfo).first()
                    print("hello",dp)
                    if dp:
                        if not dp.subcontructor_paid:
                            if not subcontructor_Address.objects.filter(user=dp).exists():
                                return redirect("sub_contructor:add_subcontructor_address")
                            else:
                                print("payment")
                                return redirect('sub_contructor:subcontructor_making_payment')
                        else:
                            return redirect('account:home-dashboard')
                    else:
                        return redirect('sub_contructor:add_subcontructor_view')
                
                
                elif userType == 'labour':
                    lc=labour_contructor.objects.filter(user=userInfo).first()
                    if  lc:
                        if not lc.labour_paid:
                            if not labour_address.objects.filter(user=lc).exists():
                                return redirect('labour_contructor:add_labour_address')
                            return redirect('labour_contructor:labour_making_payment')
                        return redirect('account:home-dashboard')    
                    return redirect('labour_contructor:add_labour_view')
                    
                #######default user
                elif userType == "user":
                    dp = user_profile.objects.filter(user=userInfo).first()
                    if dp:
                        if not dp.user_paid:
                            if not user_address.objects.filter(user=dp).exists():
                                return redirect("df_user:add_defaultuser_address")
                            else:
                                return redirect('df_user:defaultuser_making_payment')
                        else:
                            return redirect('account:home-dashboard')
                    else:
                        return redirect('df_user:add_defaultuser_view')
                
                
                else:
                    pass
            
            ### if not profile then redirect to choose profile page
            else:
                return redirect('account:choose-profile')    
        
        
        else:
            messages.success(request , 'Please enter valid otp')
            return redirect('account:verify-otp')

    context={
        'mobileNo':getMob
    }
    return render(request ,'otp-verify.html' , context)


def choose_profile(request):
    if request.POST:
        gettype = request.POST.get("chooseProfile")
        print("rol ies",gettype)
        try:
            profileofall.objects.create(
                user = request.user ,
                role = gettype
            )
            messages.success(request , 'Profile created Successfully')
            if gettype=='heavy_vehicle':
                vehicle_user_profile.objects.create(user=request.user, is_active=True)            
                return redirect('vehicle_owner:add_vehicle_view')
            elif gettype == 'driver':
                return redirect('driver:add_driver_view')
            elif gettype == 'labour':
                return redirect('labour_contructor:add_labour_view')
            elif gettype == 'subcontructor':
                print("role",gettype)
                return redirect('sub_contructor:add_subcontructor_view')
            
            elif gettype == 'user':
                return redirect('df_user:add_defaultuser_view')

        except Exception as e:
            print(e)
            messages.success(request , 'Something Went Wrong contact to admin')
            return redirect('account:choose-profile')    
                
       
    if profileofall.objects.filter(user=request.user).exists():
        getRole=profileofall.objects.filter(user=request.user).first().role
        messages.success(request , f'You have alreday registerd as {getRole}')
        deauth(request)
        return redirect('account:send-otp')         
    
    return render(request, "profile.html")


def logout_view(request):
    deauth(request)
    messages.success(request ,'You are Logout Successfully')
    return redirect('account:send-otp')

def making_payment(request):
    context={
            "merchantId": "PGTESTPAYUAT140",
            "merchantTransactionId": "MT7850590068188104",
            "merchantUserId": "MUID123",
            "amount": 1,
            "redirectUrl":"https://api-preprod.phonepe.com/apis/merchant-simulator/pg/v1/pay",
            "redirectMode": "POST",
            "callbackUrl": "https://webhook.site/callback-url",
            "mobileNumber": "8938019494",
            "paymentInstrument": {
                "type": "PAY_PAGE"
                }
                }
    return render(request ,'phonepe.html',context )
    
    
def privacypolicy(request):
    return render(request, 'conditions/Privacy.html')
    
    
def turmsconditions(request):
    return render(request, 'conditions/trurmsandconditions.html')
    
def cancelandrefund(request):
    return render(request, 'conditions/norefundandnocancelation.html')
    
    
def shippingdelivery(request):
    return render(request, 'conditions/shippingpolicy.html')
    
    
def contactus(request):
    return render(request, 'conditions/contactus.html')
    
def paymentcondition(request):
    return render(request, 'conditions/payment.html')
    