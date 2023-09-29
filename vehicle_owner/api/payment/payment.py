from all_import.all_import import *




razorpay_client = razorpay.Client(auth=("rzp_live_H6G6PNWGPU3vwq", "djfo8LPqdP6VZ4guJsN96ITb"))


############## payment gateway api ############
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication]) 
def makepaymentapi(request):
    user = vehicle_user_profile.objects.get(user=request.user)
    get_data = request.data
    get_amount = get_data['amount']
    vehicle_id = get_data['vehicle_id']
    
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
    context['vehicle_user'] = request.user.id
    vehicle_payment.objects.create(
                    user = user ,
                    razorpay_order_id = razorpay_order_id ,
                    amount = int(get_amount) ,
                    heavyvehivalregistration = heavyvehivalregistration.objects.get(id=vehicle_id)    
                )
    data = {
        'status': True ,
        'data':{
            'message': "Order Id created Successfully",
             "details": context
        }
       
    }
    return JsonResponse(data)



                              
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
# def paymenthandller(request):
#     try:
#         d_tody = date.today()
#         user = vehicle_user_profile.objects.get(user=request.user)
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
#             vehicle_payment.objects.filter(user=user, razorpay_order_id = order_id ).update(
#                 status = True,
#                 payment_id = payment_id
#             )
#             obj = vehicle_payment.objects.filter(user=user, razorpay_order_id = order_id , status=True ).first()
#             heavyvehivalregistration.objects.filter(id=obj.heavyvehivalregistration.id).update(is_paid=True ,
#                                                    expired_at=d_tody.replace(d_tody.year + 1) )
    
#         context={
#             'status': True ,
#             'data':
#             {
#                 'message': f"Payment is successfull for {obj.heavyvehivalregistration.vehicleregistrationnumber}"
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




@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def paymenthandller(request):
    try:
        d_tody = date.today()
        user = vehicle_user_profile.objects.get(user=request.user)
        get_data = request.data
        transactionId = get_data['transactionId']
        vehicleid = get_data['vehicleid']
        get_amount = vehicle_payment_amount.objects.last().value

        # verify the payment signature.
    
        # result = razorpay_client.utility.verify_payment_signature(params_dict)
        obj = vehicle_payment.objects.create(
                    user = user ,
                    razorpay_order_id = transactionId ,
                    amount = int(get_amount) ,
                    status=True,
                    heavyvehivalregistration = heavyvehivalregistration.objects.get(id=vehicleid)    
                )
        heavyvehivalregistration.objects.filter(id=obj.heavyvehivalregistration.id).update(is_paid=True ,
                                               expired_at=d_tody.replace(d_tody.year + 1) )
    
        context={
            'status': True ,
            'data':
            {
                'message': f"Payment is successfull for {obj.heavyvehivalregistration.vehicleregistrationnumber}"
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