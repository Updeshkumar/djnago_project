from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(driver_profile)
class driver_profileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "vehicalname",
        "expriencesinyear",
        "driveroperatorname",
        "Aadharnumberfrontimage",
        "Aadharnumberbackimage",
        "alternet_mobilenumber",
        "heavy_license",
        "emailId",
        "mobilenumber",
        "license_image",
        "driver_image",
        "is_active",
    ) 
@admin.register(driver_Address)
class driver_addressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state_id",
        "district_id",
        "tahseel_id",
        "is_active"
        
    ) 
admin.site.register(driver_payment_amount)
@admin.register(driver_payment)
class driver_paymentAdmin(admin.ModelAdmin):
	list_display = (
		"user",
		"razorpay_order_id",
		"amount",
		"discount",
		"status",
		"recycle",
		"created_at"
	)




class driver_paymentAdmin(admin.ModelAdmin):
	list_display = (
		"user",
		"razorpay_order_id",
		"payment_id",
		"amount",
		"discount",
		"status",
		"recycle",
		"created_at",
	)

admin.site.register(request_driver)
