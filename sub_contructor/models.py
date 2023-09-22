from django.db import models
from account.models import *




class subcontractorregistration(models.Model):
    user           = models.ForeignKey(User , on_delete=models.CASCADE)

    contractorname = models.CharField(max_length=100)
    firmname       = models.CharField(max_length=500)
    typeofwork     = models.CharField(max_length=100)
    emailId        = models.CharField(max_length=50 , null=True , blank=True)
    expriencesinyear = models.IntegerField(blank=False, null=False)
    license_number   = models.CharField(max_length=50)
    Aadharnumberfrontimage = models.ImageField(upload_to="Subcontructor-Owners/UserProfiles/")
    Aadharnumberbackimage  = models.ImageField(upload_to="Subcontructor-Owners/UserProfiles/")
    mobilenumber           = models.CharField(max_length=20)
    subcontractor_image    = models.ImageField(upload_to="Subcontructor-Owners/UserProfiles/")
    subcontractor_image_back = models.ImageField(upload_to="Subcontructor-Owners/UserProfiles/")
    subcontractor_image_left = models.ImageField(upload_to="Subcontructor-Owners/UserProfiles/")
    subcontractor_image_right = models.ImageField(upload_to="Subcontructor-Owners/UserProfiles/")
    is_active                 =    models.BooleanField(default=1,null=False)
    subcontructor_paid        = models.BooleanField(default=False)   
    expired_at                = models.DateField(null=True , blank=True)
    class Meta:
        verbose_name_plural = 'subcontructor_Profile'
        db_table = "subcontractorregistration"
    def __str__(self):
        return self.contractorname +' > '+ self.mobilenumber

        

class subcontructor_Address(models.Model):
    user = models.ForeignKey(subcontractorregistration , on_delete=models.CASCADE, related_name="SubcotructorAddress")
    state_id = models.ForeignKey(state , on_delete=models.CASCADE)
    district_id = models.ForeignKey(district , on_delete=models.CASCADE)
    tahseel_id = models.ForeignKey(tahseel , on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name_plural = 'SubContructor Address'
        db_table = 'subcontructoraddress'



class subcontructor_payment_amount(models.Model):
    value = models.IntegerField()
    
    
    class Meta:
        verbose_name_plural =  "Add  Payment For Subcontructor"
        db_table = 'subcontructor_payment_amount'



class subcontructor_payment(models.Model):
    user = models.ForeignKey(subcontractorregistration ,
                              on_delete=models.CASCADE , 
                              related_name="subcontructor_payment") 
    razorpay_order_id =  models.CharField(max_length=100)

    payment_id = models.CharField(max_length=100 , null=True , blank=True)
    
    amount =  models.IntegerField()
    discount = models.IntegerField(default=0)

    status = models.BooleanField(default=False)

    recycle = models.IntegerField(default=1)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural =  "subcontructor Payment"
        db_table = 'subcontructor_payment'

    def __str__(self):
        return self.user.user.mobile_number +'>>'+ str(self.amount)


class request_subcontructor(models.Model):
    user =  models.ForeignKey(profileofall ,  
                              on_delete=models.CASCADE ,
                              )
    subcontractorregistration = models.ForeignKey(subcontractorregistration ,  
                                                on_delete=models.CASCADE ,
                                                related_name= "requested_subcontructor"
                                                 
                                                 )
    reserved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural =  "Requested Subcontructor"
        db_table = 'request_subcontructor'

    def __str__(self):
        return self.user.user.first_name +" >>"+ self.subcontractorregistration.contractorname