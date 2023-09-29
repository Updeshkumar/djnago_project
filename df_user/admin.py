from django.contrib import admin
from .models import *



@admin.register(user_profile)
class user_profileAdmin(admin.ModelAdmin):
    list_display = (
        "user",      
	"name",      
	"is_active", 
	"user_paid", 
	"expired_at",        
    ) 

@admin.register(user_address)
class user_addressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "state_id",
        "district_id",
        "tahseel_id",
        "is_active"
        
    ) 

@admin.register(user_payment_amount)
class user_payment_amountAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'value',
    )

admin.site.register(user_payment)
