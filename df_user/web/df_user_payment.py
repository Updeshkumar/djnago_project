from all_import.all_import import *
razorpay_client = razorpay.Client(auth=("rzp_test_ytKuITMg75DwVo", "kVHhmNwyqyTBwHEuSF170xHn"))
import base64
import hashlib


razorpay_client = razorpay.Client(auth=("rzp_test_ytKuITMg75DwVo", "kVHhmNwyqyTBwHEuSF170xHn"))

@login_required(login_url='account:send-otp')

def df_user_making_payment(request): 
    user = user_profile.objects.get(user = request.user)
    get_amount = user_payment_amount.objects.last().value
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
    "redirectUrl": f"https://asiyaiheavyvehicle.com/{_path}/df_user_payhandler/",
    "redirectMode": "POST",
    "callbackUrl": "/df_user_payhandler/",
    "mobileNumber": str(request.user.mobile_number),
    "paymentInstrument": {
    "type": "PAY_PAGE"
    }
    }
    encoded=base64.urlsafe_b64encode(json.dumps(my_dict).encode()).decode()
    gg=str(encoded)+url_path+Salt_Key
    decoded_dict = str(gg).encode('utf-8')
    
    s = hashlib.sha256(decoded_dict).hexdigest()

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

    user_payment.objects.create(
                    user = user ,
                    razorpay_order_id = merchantTransactionId,
                    amount = int(get_amount) ,
                )
    context={
       "url": get_url ,
       "amount": get_amount ,
       "dfuser": user_profile.objects.filter(user = request.user).first()
    }
    # return render(request , 'payment/payment.html' , context=context) 
    return render(request , 'normal-payment.html' , context=context)



# def df_user_making_payment(request): 
#     user = user_profile.objects.get(user = request.user)
#     get_amount = user_payment_amount.objects.last().value

#     currency = 'INR'
#     amount = int(get_amount)*100   
#     # Create a Razorpay Order
#     razorpay_order = razorpay_client.order.create(dict(amount=amount,
#                                                     currency=currency,
#                                                     payment_capture='0'))
#     razorpay_order_id = razorpay_order['id']
#         # we need to pass these details to frontend.
#     _path=request.path[1:3]
#     context = {}
#     context['razorpay_order_id'] = razorpay_order_id
#     context['razorpay_merchant_key'] = "rzp_test_ytKuITMg75DwVo"
#     context['razorpay_amount'] = str(amount)
#     context['dfuser'] = user_profile.objects.get(user = request.user)

#     context['currency'] = currency
#     context['callback_url'] = f"/{_path}/df_user_payhandler/"
#     user_payment.objects.create(
#                     user = user ,
#                     razorpay_order_id = razorpay_order_id ,
#                     amount = int(get_amount) ,
#                 )
#     print(context)
#     # return render(request , 'payment/payment.html' , context=context) 
#     return render(request , 'normal-payment.html' , context=context)



@csrf_exempt
def df_user_payhandler(request):
    d_tody = date.today()
    data=request.POST
    print(data)
    if data['code'] == 'PAYMENT_SUCCESS':
        getTransaction = data['merchantOrderId']
        user_payment.objects.filter(razorpay_order_id = getTransaction ).update(
                    status = True,
                    )
        obj = user_payment.objects.filter(razorpay_order_id = getTransaction , status=True ).first()
        user_profile.objects.filter(id=obj.user.id).update(user_paid=True ,
                                                    expired_at=d_tody.replace(d_tody.year + 1) )

        return redirect('account:home-dashboard')
    else:
        print("Something went wrong ")
        messages.success(request , "Payment Failed ")
    return redirect('df_user: df_user_making_payment')



