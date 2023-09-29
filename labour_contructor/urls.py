from django.urls import path 
from labour_contructor.api.register.register import (
    labour_registration ,
    labouraddress ,
    labourdashboard 
)
from labour_contructor.api.register.update_labour import labour_update_api

from labour_contructor.api.payment.payment import labour_payment_api,labour_paymenthandller
from labour_contructor.api.requested_labour.req_labour import request_labour_api
### web import 

from labour_contructor.web.labour import add_labour_view , add_labour_address , update_labour_profile
from labour_contructor.web.dashboard import labour_dashboard , labour_view
from labour_contructor.web.labour_payment import labour_making_payment , labour_payhandler
from labour_contructor.web.labour_request import  labour_request_view


app_name = 'labour_contructor'

urlpatterns = [

    ######################################  web ################################## 
    # register and address
    path('add-labour-view/' , add_labour_view , name="add_labour_view"),
    path('add-labour-address/' , add_labour_address , name="add_labour_address"),

    # payment
    path('labour-payments/' , labour_making_payment , name="labour_making_payment") ,
    path('labour-payhandler/', labour_payhandler , name="labour_payhandler"),
    path('update-labour-profile/<int:pk>/' ,update_labour_profile , name="update_labour_profile"),

    # dash
    path('labour-web-dashboard/' , labour_dashboard , name="labour_dashboard"),
    path('labour-view/<int:pk>/' , labour_view , name="labour_view"),

    path('labour_request_view/<int:pk>/' , labour_request_view , name="labour_request_view"),
        
    #####################  APIS ###########################
    # registration , adreess and dashboard 
    path('labour-registration/' , labour_registration),
    path('labour-address/' , labouraddress),
    path('labour-dashboard/' , labourdashboard),

    # payment
    path('labour-payment/' , labour_payment_api),
    path('labour-paymenthandller/' , labour_paymenthandller),
    
    # requested labour
    path('request-labour/' , request_labour_api),
    path('labour-update-api/' , labour_update_api),

]