from django.db import models
from account.models import *
# Create your models here.
# #  labour contracot registrations

class labour_contructor(models.Model):
    user                    = models.ForeignKey(User , on_delete=models.CASCADE)
    name                    = models.CharField(max_length=100)
    labourwork              = models.CharField(max_length=500)
    emailId                 = models.CharField(max_length=100 , null=True , blank=True)
    lobourinnumber          = models.CharField(max_length=500)
    mobile_number           = models.CharField(max_length=20)
    skilledlabour           = models.IntegerField(null=False,blank=False)
    unskilledlabour         = models.IntegerField(blank=False)
    professionallabour      = models.IntegerField(null=False)
    Aadharnumberfrontimage  = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
    Aadharnumberbackimage   = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
    alternativemobilenumber = models.IntegerField(null=True , blank=True)
    labour_image            = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
    labour_paid             = models.BooleanField(default=False)   
    expired_at              = models.DateField(null=True , blank=True)
    is_active               = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural =  "Labour Contructor Profile"
        db_table = 'labour_contructor'

    def __str__(self):
        return self.name + ">"+ self.mobile_number


########### labour address ############

class labour_address(models.Model):
    user              = models.ForeignKey(labour_contructor, on_delete=models.CASCADE , related_name="labourAddress")
    state_id          = models.ForeignKey(state , on_delete=models.CASCADE)
    district_id       = models.ForeignKey(district , on_delete=models.CASCADE)
    tahseel_id        = models.ForeignKey(tahseel , on_delete=models.CASCADE)
    is_active         = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural =  "Labour Address"
        db_table = 'labouraddress'


class labour_payment_amount(models.Model):
    value = models.IntegerField()
    class Meta:
        verbose_name_plural =  "Add  Payment For Labour"
        db_table = 'labour_payment_amount'




class labour_payment(models.Model):
    user                = models.ForeignKey(labour_contructor ,
                              on_delete=models.CASCADE , 
                              related_name="labour_contructor") 
    razorpay_order_id   =  models.CharField(max_length=100)
    payment_id          = models.CharField(max_length=100 , null=True , blank=True)
    amount              =  models.IntegerField()
    discount            = models.IntegerField(default=0)
    status              = models.BooleanField(default=False)
    recycle             = models.IntegerField(default=1)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural =  "Labour Payment"
        db_table = 'labour_payment'



class request_labour(models.Model):
    user =  models.ForeignKey(profileofall ,  
                              on_delete=models.CASCADE ,
                              )
    labour_contructor = models.ForeignKey(labour_contructor ,  
                                                on_delete=models.CASCADE ,
                                                related_name= "requested_labour"
                                                 
                                                 )
    reserved = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural =  "Requested Labour"
        db_table = 'request_labour'

    def __str__(self):
        return self.user.user.first_name +" >>"+ self.labour_contructor.name
