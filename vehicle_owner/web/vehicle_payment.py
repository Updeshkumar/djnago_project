from all_import.all_import import *



def vehicle_making_payment(request , pk): 
    user = vehicle_user_profile.objects.get(user=request.user)
    get_amount = vehicle_payment_amount.objects.last().value
    vehicle_id = pk

    Salt_Key= "a30df923-b5a8-46c2-b8d7-662fea5e0b14"
    url_path = "/pg/v1/pay"
    print("request patg" , request.path)
    _path=request.path[1:3]
    print("split path",_path)
    

    #### creating  payload
    my_dict ={
    "merchantId": "ASIYAIHEAVYONLINE",
    "merchantTransactionId":f"MT{random_number()}" , 
    "merchantUserId": "MUID123",
    "amount": get_amount*100,
    "redirectUrl": f"https://asiyaiheavyvehicle.com/{_path}/vehicle-payhandler/",
    "redirectMode": "POST",
    "callbackUrl": "/vehicle-payhandler/",
    "mobileNumber": str(request.user.mobile_number),
    "paymentInstrument": {
    "type": "PAY_PAGE"
    }
    }
    encoded=base64.urlsafe_b64encode(json.dumps(my_dict).encode()).decode()
    gg=str(encoded)+url_path+Salt_Key
    decoded_dict = str(gg).encode('utf-8')
    
    s = hashlib.sha256(decoded_dict).hexdigest()
    # FOR TEST 
    # phonepe_endpoint = "https://api-preprod.phonepe.com/apis/merchant-simulator/pg/v1/pay"
    
    # For Live
    phonepe_endpoint = "https://api.phonepe.com/apis/hermes/pg/v1/pay"


    
    headers = {
        'Content-Type': 'application/json',
        'X-VERIFY': str(s)+"###1"
    }
    body ={
        'request':encoded, 
        }
    
    get_response = requests.post(phonepe_endpoint , json=body , headers=headers)
    print("Response of Phonepe Request is ::::: " , get_response.text)
    response=json.loads(get_response.text)
    get_url=""
    merchantTransactionId = response['data']['merchantTransactionId']
    get_url = response['data']['instrumentResponse']['redirectInfo']['url']

    vehicle_payment.objects.create(  
                    user = user ,
                    razorpay_order_id = merchantTransactionId,
                    amount = int(get_amount) ,
                    heavyvehivalregistration = heavyvehivalregistration.objects.get(id=vehicle_id)   
                )
    context={
       "url": get_url ,
       "amount": get_amount ,
       "vehicle":  heavyvehivalregistration.objects.get(id=pk)
    }
    return render(request , 'vehicle-payment.html' , context=context)



@csrf_exempt
def vehicle_payhandler(request):
    d_tody = date.today()
    data=request.POST
    if data['code'] == 'PAYMENT_SUCCESS':
        getTransaction = data['merchantOrderId']
        vehicle_payment.objects.filter(razorpay_order_id = getTransaction ).update(
        status = True,
        )
        obj = vehicle_payment.objects.filter(razorpay_order_id =  getTransaction, status=True ).first()
        heavyvehivalregistration.objects.filter(id=obj.heavyvehivalregistration.id).update(is_paid=True ,
                                            expired_at=d_tody.replace(d_tody.year + 1) )

        # render success page on successful caputre of payment
        messages.success(request, 'Your payment was successful')
        return redirect('account:home-dashboard')
    else:
        return redirect('account:home-dashboard')
    
    
def godashboard(request):
    return render(request, 'olddashboard.html')
        