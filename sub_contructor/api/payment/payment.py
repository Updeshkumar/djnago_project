from all_import.all_import import *




razorpay_client = razorpay.Client(auth=("rzp_live_H6G6PNWGPU3vwq", "djfo8LPqdP6VZ4guJsN96ITb"))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def subcontructor_payment_api(request):
    user = subcontractorregistration.objects.get(user=request.user)
    get_data = request.data
    get_amount = get_data['amount']
        
    currency = 'INR'
    amount = int(get_amount)*100
        
        # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                    currency=currency,
                                                    payment_capture='0'))
    razorpay_order_id = razorpay_order['id']
        # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = "rzp_live_H6G6PNWGPU3vwq"
    context['razorpay_amount'] = str(amount)
    context['currency'] = currency
    subcontructor_payment.objects.create(
                    user = user ,
                    razorpay_order_id = razorpay_order_id ,
                    amount = int(get_amount) ,  
                )
    data = {
        'status': True ,
        'data':{
            'message': "Order Id created Successfully",
             "details": context
        }
       
    }
    return JsonResponse(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def subcontructor_paymenthandller(request):
    try:
        d_tody = date.today()
        user = subcontractorregistration.objects.get(user=request.user)
        get_amount = subcontructor_payment_amount.objects.last().value
        d_tody = date.today()
        data = request.data
        transactionId = data['transactionId']

        obj = subcontructor_payment.objects.create(
                    user = user ,
                    razorpay_order_id = transactionId ,
                    amount = int(get_amount) ,  
                    status = True,
                )
        # verify the payment signature.
        # result = razorpay_client.utility.verify_payment_signature(params_dict)
    
        subcontractorregistration.objects.filter(user=request.user).update(
            subcontructor_paid=True ,
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









