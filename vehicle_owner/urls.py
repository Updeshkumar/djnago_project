from django.urls import path 
from vehicle_owner.api.register.register import (hvregistration , 
                                                 hvaddress ,
                                                 vehicle_user_data,
                                                 letest_vehicle_data
                                                 )
from vehicle_owner.api.payment.payment import makepaymentapi , paymenthandller
from vehicle_owner.api.requested_vehicle.rv import request_vehicle_api

from vehicle_owner.web.vehicle import (add_vehicle_view,
                                       add_heavy_address,
                                       get_districts ,
                                       get_tehsils ,
                                       update_vehicle,
                                       )
from vehicle_owner.api.register.update_vehicle import update_vehicle_api

from vehicle_owner.web.vehicle_payment import vehicle_making_payment , vehicle_payhandler, godashboard
from vehicle_owner.web.dashboard import vehicle_dashboard,vehicle_view
from vehicle_owner.web.vehicle_request import vehicle_request_view
app_name = 'vehicle_owner'
urlpatterns = [

    ##############    WEB  #########################################
    
    # dashboard 
    path('vehicle-dashboard/' , vehicle_dashboard , name="vehicle_dashboard"),
    path('vehicle-view/<int:pk>/' , vehicle_view , name="vehicle_view"),
    # path('vehicle-profile/' , vehicle_profile , name="vehicle_profile"),
    
    ## request vehicle
    path('vehicle_request_view/<int:pk>/' , vehicle_request_view , name="vehicle_request_view"),
    
    ## vehicle
    path('add-heavy-vehicle/' , add_vehicle_view , name="add_vehicle_view"),
    path('add-heavy-address/<int:pk>/' , add_heavy_address , name="add_heavy_address"),
    path('update-vehicle/<int:pk>/' , update_vehicle , name="update_vehicle"),
    
    path('get_districts/' , get_districts , name="get_districts") ,
    path('get_tehsils/',get_tehsils,name="get_tehsils"),
    
    path('vehicle-payment/<int:pk>/',vehicle_making_payment,name="vehicle_making_payment"),
    path('vehicle-payhandler/',vehicle_payhandler,name="vehicle_payhandler"),
    path('godashboard/', godashboard, name="godashboard"),


    ### APIs
    path('add-vehicle/', hvregistration), 
    path('add-address/', hvaddress), 
    path('vehicle-user-data/', vehicle_user_data),     
    path('letest-vehicle-data/' , letest_vehicle_data),
    path('makepayment-api/' , makepaymentapi),
    path('paymenthandller' , paymenthandller),
    path('request-vehicle/',request_vehicle_api),
    # update vehicle 
    path('update-vehicle-api/' , update_vehicle_api ) ,
    



]