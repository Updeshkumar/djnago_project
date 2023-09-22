from django.urls import path 
from .views import delete_tahseel
from account.api.register import (send_otp_mobile,
                                                 verify_mobile_otp,
                                                 add_profile,
                                                 stateListView,
                                                 districtSerializer,
                                                 tahseelSerializer

                                   
                                   )
from account.api.home.home import home_api
from account.api.search import serach_api 

from account.api.home.requirement import requirement_api , requirement_accepted_api
from account.web.home import (chooselanguage , sendotp, dumydashboard, 
                              verify_otp , 
                                choose_profile , 
                                logout_view ,
                                making_payment,
                                privacypolicy,
                                turmsconditions,
                                cancelandrefund,
                                shippingdelivery,
                                contactus,
                                paymentcondition,
                                home,
                                aboutus,
                                services,
                                contactus,
                                rentaleque,)
from account.web.dashboard import (dashboard ,
                                   vehicels_all_view,
                                   drivers_all_view,
                                   labour_all_view ,
                                   subcontructor_all_view,
                                   categories_view ,
                                   requirement_view ,
                                   requirement_req_view,
                                   requirement_cancle_view)

app_name = 'account'

urlpatterns = [
        ## WEB ############################
        path('delete_tahseel/',delete_tahseel  ),
        path('dumydashboard', dumydashboard, name='dumydashboard'),
        path('dashboard/',dashboard , name="home-dashboard" ),
        path('chooselanguage/' , chooselanguage, name="chooselanguage") ,
        path('web-send-otp/' , sendotp , name="send-otp") ,
        path('verify-otp/' , verify_otp , name="verify-otp") ,
        path('choose-profile/' , choose_profile , name="choose-profile") ,
        path('logout-view/' , logout_view , name="logout_view") ,
        path('making_payment/',making_payment, name="making_payment"),
        #View All
        path('vehicels-all-view/',vehicels_all_view, name="vehicels_all_view"),
        path('drivers-all-view/',drivers_all_view, name="drivers_all_view"),
        path('labours-all-view/',labour_all_view, name="labour_all_view"),
        path('subcontructors-all-view/',subcontructor_all_view, name="subcontructor_all_view"),

        #categories
        path('categories/',categories_view, name="categories_view"),
        # Requiremnt
        path('requirement/',requirement_view, name="requirement_view"),
        path('requirement-request/<int:pk>/',requirement_req_view, name="requirement_req_view"),
        path('requirement-cancel/<int:pk>/',requirement_cancle_view, name="requirement_cancle_view"),
        
        ## END WEB 


        ### API   
        path('send-otp/' , send_otp_mobile ) ,
        path('verify-mobile-otp/' , verify_mobile_otp ) ,
        path('add-profile/', add_profile), 
        path('states/', stateListView.as_view()),
        # path('districts/', districtSerializer.as_view()),
        path('states/<int:id>/districts/', districtSerializer.as_view()),
        path('districts/<int:id>/tahseel/', tahseelSerializer.as_view()),
        path('serach_api/', serach_api),
        
        ## Home 
        path('home-api/' , home_api) ,


        ## requirement

        path('requirement-api/' , requirement_api),
        path('requirement-accepted-api/' , requirement_accepted_api),
        
        # Add all privacy policy
        
        path('', home,),

        
        path('privacypolicy/', privacypolicy, name="privacypolicy"),
        path('turmscondition/', turmsconditions, name="turmscondition"),
        path('cancelrefund/', cancelandrefund, name="cancelrefund"),
        path('shippingdelivery/', shippingdelivery, name="shippingdelivery"),
        path('contactus/', contactus, name="contactus"),
        path('payment/', paymentcondition, name="payment"),
        path('aboutus/', aboutus, name="aboutus"),
        path('services/', services, name="services"),
        path('contactus/', contactus, name="contactus"),
        path('rentaleque/', rentaleque, name="rentaleque"),
        

        

        

    
]