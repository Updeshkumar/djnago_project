
from all_import.all_import import *

# https://api-preprod.phonepe.com/apis/merchant-simulator/pg/v1/pay



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
    
    
    
    