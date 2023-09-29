from django.urls import path 
from driver.api.register.register import driver_registration, driveraddress , driverdashboard
from driver.api.payment.payment import driver_payment_api , driver_phonepe_handller
from driver.api.register.update_driver import driver_update_api

from driver.api.requested_driver.req_driver import request_driver_api
from driver.web.driver import (
    add_driver_view ,
    add_driver_address ,
    update_driver_profile
)
from driver.web.driver_payment import driver_making_payment , driver_payhandler
from driver.web.dashboard import driver_dashboard , driver_view
from driver.web.driver_request import driver_request_view
app_name = 'driver'

urlpatterns = [
        ### WEb 
        path('add-driver/', add_driver_view , name="add_driver_view"),
        path('add-driver-address/', add_driver_address , name="add_driver_address"),
        path('update-driver-profile/<int:pk>/', update_driver_profile , name="update_driver_profile"),
        path('driver-payment/' , driver_making_payment , name="driver_making_payment") ,
        path('driver-payhandler/', driver_payhandler , name="driver_payhandler"),
        path('driver-web-dashboard/' , driver_dashboard , name="driver_dashboard"),
        path('driver-view/<int:pk>/' , driver_view , name="driver_view"),
        path('driver_request_view/<int:pk>/' , driver_request_view , name="driver_request_view"),
        ### APIS 
        path('driver-registration/' , driver_registration) ,
        path('driver_add_address/', driveraddress),
        path('driver-payment-api/' ,driver_payment_api) ,
        path('driver-phonepe-handller/' ,driver_phonepe_handller) ,
        # path('driver-paymenthandller/' ,driver_paymenthandller) ,
        path('driver-dashboard/' ,driverdashboard ) ,
        path('request-driver/' , request_driver_api),
        path('driver-update-api/' , driver_update_api),
]