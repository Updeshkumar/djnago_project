from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(labour_contructor)
class labou_contructorAdmin(admin.ModelAdmin):
	list_display = (
		"user",                   
                "name",                   
		"labourwork",             
		"emailId",
		"lobourinnumber",         
		"mobile_number",          
		"skilledlabour",          
		"unskilledlabour",        
		"professionallabour",     
		"Aadharnumberfrontimage", 
		"Aadharnumberbackimage",  
		"alternativemobilenumber",
		"labour_image",           
		"labour_paid",            
		"expired_at",             
		"is_active",              
	)

@admin.register(labour_address)
class labour_addressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state_id",
        "district_id",
        "tahseel_id",
        "is_active"
        
    ) 
admin.site.register(labour_payment_amount)
@admin.register(labour_payment)
class labour_paymentAdmin(admin.ModelAdmin):
	list_display = (
		"user",
		"razorpay_order_id",
		"amount",
		"discount",
		"status",
		"recycle",
		"created_at"
	)



@admin.register(request_labour)
class request_labourAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "labour_contructor",
        "reserved",
    )
    list_filter = ('user' , )    
