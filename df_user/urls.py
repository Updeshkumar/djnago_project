from django.urls import path 


#### api import
from df_user.api.register.register import defaultuser_registration ,defaultuser_Address , defaultuserdashboard
from df_user.api.payment.payment import defaultuser_payment_api , defaultuser_paymenthandller



from df_user.web.register.register import (
    add_defaultuser_view ,
    add_defaultuser_address 
)
from df_user.web.df_user_payment import df_user_making_payment,df_user_payhandler


app_name = 'df_user'

urlpatterns = [
    
    ###### start api user ###### 
    
    path('dfuser-registration/' , defaultuser_registration) ,
    path('dfuser_Address/', defaultuser_Address),
    path('dfuser-payment-api/' ,defaultuser_payment_api) ,
    path('dfuser-paymenthandller/' ,defaultuser_paymenthandller) ,
    path('dfuser-dashboard/' ,defaultuserdashboard ) ,


     ###### end api user ###### 
    
    
    
    path('add-defaultuser-view/' , add_defaultuser_view , name="add_defaultuser_view"),
    path('add-defaultuser-address/' , add_defaultuser_address , name="add_defaultuser_address"),
    path('df_user_making_payment/', df_user_making_payment, name="df_user_making_payment"),
    path('df_user_payhandler/', df_user_payhandler, name="df_user_payhandler")

   
    
]