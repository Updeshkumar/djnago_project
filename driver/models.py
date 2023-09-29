from django.db import models
from account.models import *


#############driver operator registrations class #####################
class driver_profile(models.Model):
    user                    = models.ForeignKey(User , on_delete=models.CASCADE)
    vehicalname             = models.CharField(max_length=200)
    expriencesinyear        = models.IntegerField(blank=False, null=False)
    driveroperatorname      = models.CharField(max_length=200)
    Aadharnumberfrontimage  = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
    Aadharnumberbackimage   = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
    alternet_mobilenumber   = models.CharField(max_length=12 ,  null=True , blank=True)
    heavy_license           = models.CharField(max_length=50)
    emailId                 = models.EmailField(max_length=100 , null=True , blank=True)
    mobilenumber            = models.CharField(max_length=20)
    license_image           = models. ImageField(upload_to="static/Uploaded/UserProfiles/")
    driver_image            = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
    is_active               = models.BooleanField(default=True)
    driver_paid             = models.BooleanField(default=False)   
    expired_at              = models.DateField(null=True , blank=True)
    class Meta:
        verbose_name_plural = 'Driver Profile'
        db_table = "driveroperatorregistration"
    def __str__(self):
        return self.driveroperatorname +' > '+ self.mobilenumber


############ driver addresss ##############
class driver_Address(models.Model):
    user = models.ForeignKey(driver_profile , on_delete=models.CASCADE, related_name="driverAddress")
    state_id = models.ForeignKey(state , on_delete=models.CASCADE)
    district_id = models.ForeignKey(district , on_delete=models.CASCADE)
    tahseel_id = models.ForeignKey(tahseel , on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name_plural = 'Driver Address'
        db_table = 'driveraddress'


class driver_payment_amount(models.Model):
    value = models.IntegerField()
    
    
    class Meta:
        verbose_name_plural =  "Add  Payment For Driver"
        db_table = 'driver_payment_amount'



class driver_payment(models.Model):
    user = models.ForeignKey(driver_profile ,
                              on_delete=models.CASCADE , 
                              related_name="driver_payment") 
    razorpay_order_id =  models.CharField(max_length=100)

    payment_id = models.CharField(max_length=100 , null=True , blank=True)
    
    amount =  models.IntegerField()
    discount = models.IntegerField(default=0)

    status = models.BooleanField(default=False)

    recycle = models.IntegerField(default=1)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural =  "Driver Payment"
        db_table = 'driver_payment'


class request_driver(models.Model):
    user =  models.ForeignKey(profileofall ,  
                              on_delete=models.CASCADE ,
                              )
    driver_profile = models.ForeignKey(driver_profile ,  
                                                on_delete=models.CASCADE ,
                                                related_name= "requested_driver"
                                                 
                                                 )
    reserved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural =  "Requested Driver"
        db_table = 'request_driver'

    def __str__(self):
        return self.user.user.first_name +" >>"+ self.driver_profile.driveroperatorname