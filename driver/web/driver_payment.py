from all_import.all_import import *
razorpay_client = razorpay.Client(auth=("rzp_test_ytKuITMg75DwVo", "kVHhmNwyqyTBwHEuSF170xHn"))
import base64
import hashlib


@login_required(login_url='account:send-otp')
def driver_making_payment(request): 
    user = driver_profile.objects.get(user=request.user) 
    get_amount=driver_payment_amount.objects.last().value 
    Salt_Key= "a30df923-b5a8-46c2-b8d7-662fea5e0b14"
    url_path = "/pg/v1/pay"

    _path=request.path[1:3]
    print(_path)
    

    #### creating  payload
    my_dict ={
    "merchantId": "ASIYAIHEAVYONLINE",
    "merchantTransactionId":f"MT{random_number()}" , 
    "merchantUserId": "MUID123",
    "amount": get_amount*100,
    "redirectUrl": f"https://asiyaiheavyvehicle.com/{_path}/driver-payhandler/",
    "redirectMode": "POST",
    "callbackUrl": "/driver-payhandler/",
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

    driver_payment.objects.create(  
                    user = user ,
                    razorpay_order_id = merchantTransactionId,
                    amount = int(get_amount) ,
                )
    context={
       "url": get_url ,
       "amount": get_amount ,
       "driver": driver_profile.objects.filter(user = request.user).first()
    }

    return render(request , 'driver-payment.html' , context=context)


@csrf_exempt
def driver_payhandler(request):
    print("POST REQUESTTTTTTTTTTTTTTTTTTTTTT",request.POST)

    d_tody = date.today()
    data=request.POST
    if data['code'] == 'PAYMENT_SUCCESS':
        getTransaction = data['merchantOrderId']
        driver_payment.objects.filter(razorpay_order_id = getTransaction ).update(
                    status = True,
                    )
        obj = driver_payment.objects.filter(razorpay_order_id = getTransaction , status=True ).first()
        driver_profile.objects.filter(id=obj.user.id).update(driver_paid=True ,
                                                        expired_at=d_tody.replace(d_tody.year + 1) )
        
        return redirect('account:home-dashboard')
    else:
        print("Something went wrong ")
        messages.success(request , "Payment Failed ")
        return redirect('driver:driver_making_payment')


#  <QueryDict: {'code': ['PAYMENT_SUCCESS'], 
#               'merchantId': ['ASIYAIHEAVYONLINE'], 
#               'transactionId': ['MT7850590068188114'],
#                 'amount': ['100'], 
#                 'providerReferenceId': ['T2306191625398007140382'], 
#                 'param1': ['na'], 'param2': ['na'], 'param3': ['na'], 'param4': ['na'], 
#                 'param5': ['na'], 'param6': ['na'], 'param7': ['na'], 'param8': ['na'],
#                   'param9': ['na'], 'param10': ['na'], 'param11': ['na'], 'param12': ['na'], 
#                   'param13': ['na'], 'param14': ['na'], 'param15': ['na'], 'param16': ['na'],
#                     'param17': ['na'], 'param18': ['na'], 'param19': ['na'], 'param20': ['na'], 
#               'checksum': ['1404c018fd576b0fe458d7b3c1d545d4b0b39c249fb556a7d0ac09a3c3d13360###1']}>
# def driver_making_payment(request): 
#     user = driver_profile.objects.get(user=request.user)
#     get_amount = driver_payment_amount.objects.last().value
    
#     currency = 'INR'
#     amount = int(get_amount)*100   
#     # Create a Razorpay Order
#     razorpay_order = razorpay_client.order.create(dict(amount=amount,
#                                                     currency=currency,
#                                                     payment_capture='0'))
#     razorpay_order_id = razorpay_order['id']
#         # we need to pass these details to frontend.
#     _path=request.path[1:3]
#     print(_path)
#     context = {}
#     context['razorpay_order_id'] = razorpay_order_id
#     context['razorpay_merchant_key'] = "rzp_test_ytKuITMg75DwVo"
#     context['razorpay_amount'] = str(amount)
#     context['amount'] = str(get_amount)
#     context['currency'] = currency
#     context['full_path'] = request.path
#     context['driver'] = driver_profile.objects.get(user = request.user)

#     context['path'] = _path
#     context['callback_url'] = f"/{_path}/driver-payhandler/"
#     driver_payment.objects.create(  
#                     user = user ,
#                     razorpay_order_id = razorpay_order_id ,
#                     amount = int(get_amount) ,
#                 )
#     return render(request , 'driver-payment.html' , context=context)


# {'code': ['PAYMENT_SUCCESS'], 
# 'merchantId': ['PGTESTPAYUAT91'], 
# 'transactionId': ['MT7850590068188114'], 
# 'amount': ['10000'], 
# 'providerReferenceId': 
# ['T2306151744467057656085'], 
# 'param1': ['na'], 'param2': ['na'], 
# 'param3': ['na'], 'param4': ['na'], 'param5': ['na'], 
# 'param6': ['na'], 'param7': ['na'], 'param8': ['na'], 
# 'param9': ['na'], 'param10': ['na'], 'param11': ['na'], 
# 'param12': ['na'], 'param13': ['na'], 'param14': ['na'], 
# 'param15': ['na'], 'param16': ['na'], 'param17': ['na'],
#  'param18': ['na'], 'param19': ['na'], 'param20': ['na'],
#  'checksum': ['2ec420101ce340d500564d384adb5625accf5354bedcfa4588a9a4d915c2dbd0###1']}>



# @csrf_exempt
# def driver_payhandler(request):
#     d_tody = date.today()
#     if request.method == "POST":
#         print("request is", request.POST)
#         payment_id = request.POST.get('razorpay_payment_id', '')
#         order_id = request.POST.get('razorpay_order_id', '')
#         signature = request.POST.get('razorpay_signature', '')

#         print(payment_id,order_id,signature)
#         params_dict = {
#                 'razorpay_order_id': order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#         }
#         result = razorpay_client.utility.verify_payment_signature(
#                 params_dict)
       
#         if result is not None:
#             try:
                
#                 # capture the payemt
#                 # razorpay_client.payment.capture(payment_id, amount)
#                 # print("amount is " , amount)
#                 driver_payment.objects.filter(razorpay_order_id = order_id ).update(
#                 status = True,
#                 payment_id = payment_id
#                 )
#                 obj = driver_payment.objects.filter(razorpay_order_id = order_id , status=True ).first()
#                 driver_profile.objects.filter(id=obj.user.id).update(driver_paid=True ,
#                                                     expired_at=d_tody.replace(d_tody.year + 1) )

#                 # render success page on successful caputre of payment
#                 messages.success(request, 'Your payment was successful')
#                 return redirect('account:home-dashboard')
#             except Exception as e:
#                 print("exception",e)
#                 messages.error(request, 'Something went wrong!!')
#                 return redirect('')
#         else:
#             print(result)
#             messages.error(request, 'Something went wrong!!')
#             return redirect('/')


    