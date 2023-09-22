from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(vehicle_user_profile)

@admin.register(heavyvehivalregistration)
class heavyvehivalregistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        'vehical_name',
        'company_name',
        'emailId',
        'ownername',
        'vehicleregistrationnumber',
        'Aadharnumberfrontimage',
        'Aadharnumberbackimage',
        'vehicle_image',
        'vehicle_image_back',
        'vehicle_image_left',
        'vehicle_image_right',
        'manufacture_date',
        'alternativemobilenumber',
        'vehiclemodelnumber',
        'is_paid',
        'is_active',
        'created_at',
        'updated_at',
        
        
    ) 

@admin.register(heavyvehicleaddress)
class heavyvehicleaddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state_id",
        "district_id",
        "tahseel_id",
        "is_active"
        
    ) 
admin.site.register(vehicle_payment_amount)
admin.site.register(discount_coupon)
admin.site.register(user_coupon)
@admin.register(vehicle_payment)
class vehicle_paymentAdmin(admin.ModelAdmin):
	 list_display = (
        "id",
        "user",
        "razorpay_order_id",
        "payment_id",
        "amount",
	"discount",
	"heavyvehivalregistration",
	"status",
	"recycle",
	"created_at"
        
    ) 


@admin.register(request_vehicle)
class request_vehicleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "heavyvehivalregistration",
        "reserved",
    )
    list_filter = ('user' , )    