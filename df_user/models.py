from django.db import models
from account.models import *



class user_profile(models.Model):
    user              = models.ForeignKey(User , on_delete=models.CASCADE )
    name              = models.CharField(max_length=50)
    is_active         = models.BooleanField(default=True)
    user_paid         = models.BooleanField(default=False)   
    expired_at        = models.DateField(null=True , blank=True)

    def __str__(self):
        return self.name +""+ self.user.mobile_number
    

    class Meta:
        verbose_name_plural = 'User Profile'
        db_table = 'user_profile'

    

class user_address(models.Model):
    user = models.ForeignKey(user_profile , on_delete=models.CASCADE , related_name="userAddress")
    state_id = models.ForeignKey(state , on_delete=models.CASCADE)
    district_id = models.ForeignKey(district , on_delete=models.CASCADE)
    tahseel_id = models.ForeignKey(tahseel , on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name_plural = 'User Address'
        db_table = 'user_address'


class user_payment_amount(models.Model):
    value = models.IntegerField()
    
    class Meta:
        verbose_name_plural =  "Add  Payment For General User"
        db_table = 'user_payment_amount'



class user_payment(models.Model):
    user = models.ForeignKey(user_profile ,
                              on_delete=models.CASCADE , 
                              related_name="user_payment") 
    razorpay_order_id =  models.CharField(max_length=100)

    payment_id = models.CharField(max_length=100 , null=True , blank=True)
    
    amount =  models.IntegerField()
    discount = models.IntegerField(default=0)

    status = models.BooleanField(default=False)

    recycle = models.IntegerField(default=1)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural =  "General User Recieved Payment"
        db_table = 'user_payment'   





