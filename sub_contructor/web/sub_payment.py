from all_import.all_import import *
razorpay_client = razorpay.Client(auth=("rzp_test_ytKuITMg75DwVo", "kVHhmNwyqyTBwHEuSF170xHn"))
import base64
import hashlib



razorpay_client = razorpay.Client(auth=("rzp_test_ytKuITMg75DwVo", "kVHhmNwyqyTBwHEuSF170xHn"))


@login_required(login_url='account:send-otp')
def subcontructor_making_payment(request): 
    user = subcontractorregistration.objects.get(user = request.user)
    get_amount = subcontructor_payment_amount.objects.last().value
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
    "redirectUrl": f"https://asiyaiheavyvehicle.com/{_path}/subcontructor-payhandler/",
    "redirectMode": "POST",
    "callbackUrl": "/subcontructor-payhandler/",
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

    subcontructor_payment.objects.create(
                    user = user ,
                    razorpay_order_id = merchantTransactionId,
                    amount = int(get_amount) ,
                )
    context={
       "url": get_url ,
       "amount": get_amount ,
       "subcontructor": subcontractorregistration.objects.filter(user = request.user).first()
    }
    # return render(request , 'payment/payment.html' , context=context) 
    return render(request , 'subcontructor-payment.html' , context=context)



@csrf_exempt
def subcontrctor_payhandler(request):
    d_tody = date.today()
    data=request.POST
    if data['code'] == 'PAYMENT_SUCCESS':
        getTransaction = data['merchantOrderId']
        subcontructor_payment.objects.filter(razorpay_order_id = getTransaction ).update(
                    status = True,
                    )
        obj = subcontructor_payment.objects.filter(razorpay_order_id = getTransaction , status=True ).first()
        subcontractorregistration.objects.filter(id=obj.user.id).update(subcontructor_paid=True ,
                                                    expired_at=d_tody.replace(d_tody.year + 1) )

        return redirect('account:home-dashboard')
    else:
        print("Something went wrong ")
        messages.success(request , "Payment Failed ")
        return redirect('sub_contructor:subcontructor_making_payment')



# @csrf_exempt
# def subcontrctor_payhandler(request):
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
#                 subcontructor_payment.objects.filter(razorpay_order_id = order_id ).update(
#                 status = True,
#                 payment_id = payment_id
#                 )
#                 obj = subcontructor_payment.objects.filter(razorpay_order_id = order_id , status=True ).first()
#                 subcontractorregistration.objects.filter(id=obj.user.id).update(subcontructor_paid=True ,
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


    