from all_import.all_import import *


@login_required(login_url='account:send-otp')
def labour_making_payment(request): 
    user = labour_contructor.objects.get(user=request.user)
    get_amount = labour_payment_amount.objects.last().value
    
    Salt_Key= "a30df923-b5a8-46c2-b8d7-662fea5e0b14"
    url_path = "/pg/v1/pay"
    
    _path=request.path[1:3]
    print(_path)
    
    #### creating  payload
    print(f"MT{random_number()}")
    my_dict ={
    "merchantId": "ASIYAIHEAVYONLINE",
    "merchantTransactionId":f"MT{random_number()}" , 
    "merchantUserId": "MUID123",
    "amount": get_amount*100,
    "redirectUrl": f"https://asiyaiheavyvehicle.com/{_path}/labour-payhandler/",
    "redirectMode": "POST",
    "callbackUrl": "/labour-payhandler/",
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

    labour_payment.objects.create(  
                    user = user ,
                    razorpay_order_id = merchantTransactionId,
                    amount = int(get_amount) ,
                )
    context={
       "url": get_url ,
       "amount": get_amount ,
       "labour": user
    }

    return render(request , 'labour-payment.html' , context=context)


@csrf_exempt
def labour_payhandler(request):
    print("POST REQUESTTTTTTTTTTTTTTTTTTTTTT",request.POST)

    d_tody = date.today()
    data=request.POST
    if data['code'] == 'PAYMENT_SUCCESS':
        getTransaction = data['merchantOrderId']
        labour_payment.objects.filter(razorpay_order_id = getTransaction ).update(
                    status = True,
                    )
        obj = labour_payment.objects.filter(razorpay_order_id = getTransaction , status=True ).first()
        labour_contructor.objects.filter(id=obj.user.id).update(labour_paid=True ,
                                                        expired_at=d_tody.replace(d_tody.year + 1) )
        
        return redirect('account:home-dashboard')
    else:
        print("Something went wrong ")
        messages.success(request , "Payment Failed ")
        return redirect('labour_contructor:labour_making_payment')



