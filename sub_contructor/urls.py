from django.urls import path 


from sub_contructor.api.register.register import subcontructor_registration ,subcontructor_Address , subcontructordashboard
from sub_contructor.api.payment.payment import subcontructor_payment_api , subcontructor_paymenthandller
from sub_contructor.api.requested_subcon.req_subcon import request_subcontructor_api
from sub_contructor.api.register.update_subcontructor import subcontructor_update_api


## WEB URLS IMORT

from sub_contructor.web.sub import add_subcontructor_view , add_subcontructor_address, update_subcotructor_profile
from sub_contructor.web.sub_payment import subcontructor_making_payment,subcontrctor_payhandler
from sub_contructor.web.subconturctor_request import request_subcontructor_view
from sub_contructor.web.dashboard import subcontructor_dashboard , subcontructor_view



# from driver.api.payment.payment import driver_paymenthandller , driver_payment_api
app_name = 'sub_contructor'

urlpatterns = [
        
        ## Web 

        path('add-subcontructor/' , add_subcontructor_view , name="add_subcontructor_view"),
        path('add-subcontructor-address/' , add_subcontructor_address , name="add_subcontructor_address"),
        path('update-subcontructor-profile/<int:pk>/' , update_subcotructor_profile , name="update_subcotructor_profile"),

        path('subcontructor-view/<int:pk>/' , subcontructor_view , name="subcontructor_view"),
        path('subcontructor_request_view/<int:pk>/' , request_subcontructor_view , name="subcontructor_request_view"),

        path('subcontructor-web-dashboard/' , subcontructor_dashboard , name="subcontructor_dashboard"),

        path('subcontructor-payment/' , subcontructor_making_payment , name="subcontructor_making_payment"),
        path('subcontructor-payhandler/', subcontrctor_payhandler , name="subcontrctor_payhandler"),

        

        ## APIS

        path('subcontructor-registration/' , subcontructor_registration) ,
        path('subcontructor_Address/', subcontructor_Address),
        path('subcontructor-payment-api/' ,subcontructor_payment_api) ,
        path('subcontructor-paymenthandller/' ,subcontructor_paymenthandller) ,
        path('request-subcontructor/' , request_subcontructor_api) ,
        path('subcontructor-dashboard/' ,subcontructordashboard ) ,
        path('subcontructor_update_api/' , subcontructor_update_api),


]