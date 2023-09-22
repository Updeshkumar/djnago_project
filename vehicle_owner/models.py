from django.db import models
from account.models import *



class vehicle_user_profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.mobile_number



class heavyvehivalregistration(models.Model):
    user                      = models.ForeignKey(vehicle_user_profile , on_delete=models.CASCADE , related_name="vehicle_owners")
    vehical_name              = models.CharField(max_length=200)
    company_name              = models.CharField(max_length = 100)
    emailId                   = models.CharField(max_length=50)
    ownername                 = models.CharField(max_length=300)
    vehicleregistrationnumber = models.CharField(max_length=100)
    Aadharnumberfrontimage    = models.ImageField(upload_to="Vehicle-Owners/UserProfiles/")
    Aadharnumberbackimage     = models.ImageField(upload_to="Vehicle-Owners/UserProfiles/")
    vehicle_image             = models.ImageField(upload_to="Vehicle-Owners/UserProfiles/")
    vehicle_image_back        = models.ImageField(upload_to="Vehicle-Owners/UserProfiles/")
    vehicle_image_left        = models.ImageField(upload_to="Vehicle-Owners/UserProfiles/")
    vehicle_image_right       = models.ImageField(upload_to="Vehicle-Owners/UserProfiles/")
    manufacture_date          = models.DateField()
    alternativemobilenumber   = models.CharField(max_length=20)
    vehiclemodelnumber        = models.CharField(max_length=100)
    expired_at                = models.DateField(null=True , blank=True)
    is_paid                   = models.BooleanField(default=False)
    is_active                 = models.BooleanField(default=True)

    created_at                = models.DateTimeField(auto_now_add=True)
    updated_at                = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.user.mobile_number) +" "+ self.vehical_name 
    
    class Meta:
        verbose_name_plural =  "Heavy Vehicle"
        db_table = "heavyvehivalregistration"



class heavyvehicleaddress(models.Model):
    user = models.ForeignKey(vehicle_user_profile ,
                              on_delete=models.CASCADE ,
                                related_name="vehicle_address")
    heavyvehivalregistration = models.ForeignKey(heavyvehivalregistration, on_delete=models.CASCADE, related_name="vehicleaddress")
    state_id = models.ForeignKey(state , on_delete=models.CASCADE)
    district_id = models.ForeignKey(district , on_delete=models.CASCADE)
    tahseel_id = models.ForeignKey(tahseel , on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural =  "Vehicle Address"
        db_table = 'heavyvehicleaddress'


class vehicle_payment_amount(models.Model):
    value = models.IntegerField()
    
    
    class Meta:
        verbose_name_plural =  "Add  Payment For Vehicle "
        db_table = 'payment_amount'




class discount_coupon(models.Model):
    value = models.IntegerField()

class user_coupon(models.Model):
    user = models.ForeignKey(User ,  on_delete=models.CASCADE)
    discount_coupon = models.ForeignKey(discount_coupon ,  on_delete=models.CASCADE)
    expiry = models.DateField()



class vehicle_payment(models.Model):
    user = models.ForeignKey(vehicle_user_profile ,
                              on_delete=models.CASCADE , 
                              related_name="vehicle_payments") 
    razorpay_order_id =  models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100 , null=True , blank=True)
    
    amount =  models.IntegerField()
    discount = models.IntegerField(default=0)
    heavyvehivalregistration = models.ForeignKey(heavyvehivalregistration ,  on_delete=models.CASCADE) 
    status = models.BooleanField(default=False)

    recycle = models.IntegerField(default=1)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    

class request_vehicle(models.Model):
    user =  models.ForeignKey(profileofall ,  
                              on_delete=models.CASCADE ,
                              related_name= "requested_user" ,
                              )
    heavyvehivalregistration = models.ForeignKey(heavyvehivalregistration ,  
                                                on_delete=models.CASCADE ,
                                                related_name= "requested_vehicle"
                                                 
                                                 )
    reserved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural =  "Requested Vehicle"
        db_table = 'request_vehicle'

    def __str__(self):
        return self.user.user.first_name +" "+ self.heavyvehivalregistration.vehical_name



    
