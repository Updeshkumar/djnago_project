from django.contrib import admin
from .models import *

@admin.register(subcontractorregistration)
class subcontractorregistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "contractorname",
        "firmname",
        "typeofwork",
        "emailId",
        "expriencesinyear",
        "license_number",
        "Aadharnumberfrontimage",
        "Aadharnumberbackimage",
        "mobilenumber",
        "subcontractor_image",
        "subcontractor_image_back",
        "subcontractor_image_left",
        "subcontractor_image_right",
        "is_active",
        "subcontructor_paid",
        "expired_at",
        
    ) 

    def __str__(self):
        return self.contractorname

@admin.register(subcontructor_Address)
class subcontructor_AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state_id",
        "district_id",
        "tahseel_id",
        "is_active"
        
    ) 

admin.site.register(subcontructor_payment_amount)
@admin.register(subcontructor_payment)
class subcontructor_paymentAdmin(admin.ModelAdmin):
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

admin.site.register(request_subcontructor)

