from all_import.all_import import *



############## payment gateway api ############


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def driver_payment_api(request):
    user = driver_profile.objects.get(user=request.user) 
    get_amount=driver_payment_amount.objects.last().value 
    Salt_Key= "a30df923-b5a8-46c2-b8d7-662fea5e0b14"
    url_path = "/pg/v1/pay"


    #### creating  payload
    my_dict ={
    "merchantId": "ASIYAIHEAVYONLINE",
    "merchantTransactionId":f"MT{random_number()}" , 
    "merchantUserId": "MUID123",
    "amount": get_amount*100,
    "redirectUrl": f"http://asiyaiheavyvehicle.com/en/driver-phonepe-handller/",
    "redirectMode": "POST",
    "callbackUrl": "/driver-payhandler/",
    "mobileNumber": str(request.user.mobile_number),
    "user_id": f"{request.user.id}",
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
        'status': True ,
        'data':{
            "msg": "Payment Page Genetated Successfully"     ,
            "url": get_url ,
            "amount": get_amount 
            }
    }

    return JsonResponse(context)
    #return render(request , 'driver-payment.html' , context=context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def driver_phonepe_handller(request):
    try:
        user = driver_profile.objects.get(user=request.user) 
        get_amount=driver_payment_amount.objects.last().value 
        d_tody = date.today()
        data = request.data
        transactionId = data['transactionId']
        
        obj = driver_payment.objects.create(  
                    user = user ,
                    razorpay_order_id = transactionId,
                    amount = int(get_amount) ,
                    status=True
                )
        
        driver_profile.objects.filter(id=obj.user.id).update(
                                                                    driver_paid=True ,
                                                                    expired_at=d_tody.replace(d_tody.year + 1) 
                                                                )
        context={
            'status': True ,
            'data':
            {
                'message': f"Payment is successfull"
            }
        }
        return JsonResponse(context)
    except Exception as e:
        context={
            'status': False ,
            'data':
            {
                'message': f"{e}"
            }
        }
        return JsonResponse(context)






# from all_import.all_import import *




# razorpay_client = razorpay.Client(auth=("rzp_live_H6G6PNWGPU3vwq", "djfo8LPqdP6VZ4guJsN96ITb"))


# ############## payment gateway api ############
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication]) 
# def driver_payment_api(request):
#     user = driver_profile.objects.get(user=request.user)
#     get_data = request.data
#     get_amount = get_data['amount']
        
#     currency = 'INR'
#     amount = int(get_amount)*100
        
#         # Create a Razorpay Order
#     razorpay_order = razorpay_client.order.create(dict(amount=amount,
#                                                     currency=currency,
#                                                     payment_capture='0'))
#     razorpay_order_id = razorpay_order['id']
#         # we need to pass these details to frontend.
#     context = {}
#     context['razorpay_order_id'] = razorpay_order_id
#     context['razorpay_merchant_key'] = "rzp_live_H6G6PNWGPU3vwq"
#     context['razorpay_amount'] = str(amount)
#     context['currency'] = currency
#     driver_payment.objects.create(
#                     user = user ,
#                     razorpay_order_id = razorpay_order_id ,
#                     amount = int(get_amount) ,  
#                 )
#     data = {
#         'status': True ,
#         'data':{
#             'message': "Order Id created Successfully",
#              "details": context
#         }
       
#     }
#     return JsonResponse(data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# def driver_paymenthandller(request):
#     try:
#         d_tody = date.today()
#         user = driver_profile.objects.get(user=request.user)
#         get_data = request.data
#         order_id = get_data['order_id']
#         payment_id = get_data['payment_id']
#         signature = get_data['signature']

#         params_dict = {
#                 'razorpay_order_id': order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature 
#             }
#         # verify the payment signature.
    
#         # result = razorpay_client.utility.verify_payment_signature(params_dict)
#         result = None
#         if result is None:
#             driver_payment.objects.filter(user=user, razorpay_order_id = order_id ).update(
#                 status = True,
#                 payment_id = payment_id
#             )
            
#             driver_profile.objects.filter(user=request.user).update(driver_paid=True ,
#                                                                     expired_at=d_tody.replace(d_tody.year + 1) )
        
#         context={
#             'status': True ,
#             'data':
#             {
#                 'message': f"Payment is successfull"
#             }
#         }
#         return JsonResponse(context)
#     except Exception as e:
#         context={
#             'status': False ,
#             'data':
#             {
#                 'message': f"{e}"
#             }
#         }
#         return JsonResponse(context)




