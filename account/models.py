from django.db import models
from rest_framework import status
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.core.validators import RegexValidator




class UserManager(BaseUserManager):
    def create_user(self, mobile_number, password=None, is_staff=False, is_active=True, is_admin=False):
        if not mobile_number:
            raise ValueError('users must have a phone number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(
            mobile_number=mobile_number
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, mobile_number, password=None):
        user = self.create_user(
            mobile_number,
            password=password,
            is_staff=True,


        )
        return user

    def create_superuser(self, mobile_number, password=None):
        user = self.create_user(
            mobile_number,
            password=password,
            is_staff=True,
            is_admin=True,


        )
        return user


    


class User(AbstractBaseUser,PermissionsMixin):
    user_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    country_code = models.IntegerField(default=91,)
    mobile_number = models.CharField(max_length=20, unique=True)
    otp = models.CharField(max_length=4,null=True,blank=True)
    
    updated_by = models.IntegerField(default=False, null=True)
    email_id = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=20,null=False,blank=False, default="USER")
    profile_pic = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    
    active = models.BooleanField(default=1,null=False)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    
    is_delete = models.BooleanField(default=0,null=False)
    gender = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    
    class Meta:
        db_table = 'user'

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.mobile_number

    def get_full_name(self):
        return self.mobile_number

    def get_short_name(self):
        return self.mobile_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



class profileofall(models.Model):
    roletype = (
        (
        "heavy_vehicle","heavy_vehicle",
        ),
                (
        "driver","driver",
        ),
                (
        "subcontructor","subcontructor",
        ),
                (
        "labour","labour",
        ),
         (
        "user","user",
        ),

    )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=roletype)

    def __str__(self):
        return self.user.mobile_number 



    

    



class Account_Pending(models.Model):
    phone_regex     = RegexValidator( regex   =r'^\+?1?\d{9,14}$', message ="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.")
    phone           = models.CharField(validators=[phone_regex], max_length=17,) 
    otp             = models.PositiveIntegerField(blank = True, null = True)
    role            = models.CharField(max_length=20, blank = True, null = True)
    is_verified     = models.BooleanField(default=False)
    is_registered   = models.BooleanField(default=False)

    def __str__(self):
        return str(self.phone)


class state(models.Model):
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name

    class Meta:
        verbose_name_plural =  "States"
        db_table = 'state'

class district(models.Model):
    state_id = models.ForeignKey(state , on_delete=models.CASCADE , related_name='state_district')
    district_name = models.CharField(max_length=100)

    def __str__(self):
        return self.district_name

    class Meta:
        verbose_name_plural =  "Districts"
        db_table = 'district'
        
class tahseel(models.Model):
    district_id = models.ForeignKey(district , on_delete=models.CASCADE , related_name='district_city')
    tahseel_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tahseel_name

    class Meta:
        verbose_name_plural =  "Tahseel"
        db_table = 'tahseel'




# #  This class is use for create the preference model
# class Device(models.Model):

#     device_id = models.AutoField(primary_key=True)
#     refresh_token = models.CharField(max_length=500,default=False, null=True)
#     device_type = models.CharField(max_length=20)
#     device_token = models.CharField(max_length=255,default=False, null=True)
#     aws_arn = models.CharField(max_length=255, null=True)
#     created_by =  models.ForeignKey(User, db_column = 'created_by',related_name='device_user', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=1,null=False)
    
#     class Meta:
#         db_table = 'device'









# ################ Normal User Registration ########
# class NormalUser(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE)

#     name = models.CharField(max_length=100)
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)



#     class Meta:
#         db_table = "normaluser"


#             # ###################Heavy Vehical Registrations #####################
# class profileofall(models.Model):
#     roletype = (
#         (
#             "heavy_vehicle","heavy_vehicle",
#         ),
#         (
#             "driver","driver",
#         ),
#         (
#             "subcotructor","subcotructor",
#         ),
#         (
#             "labour","labour",
#         ),

#     )
#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=roletype)
    


# class heavyvehicleaddress(models.Model):
#     user_id = models.IntegerField(default=0)
#     heavyvehivalregistration = models.ForeignKey(heavyvehivalregistration, on_delete=models.CASCADE)
#     state_id = models.CharField(max_length=20)
#     district_id = models.CharField(max_length=20)
#     city_id = models.CharField(max_length=20)
#     is_active = models.BooleanField(default=1,null=False)
    

#     class Meta:
#         db_table = 'heavyvehicleaddress'





# class Request_Heavy_Vehical(models.Model):
#     heavyvehicleaddress = models.ForeignKey(heavyvehicleaddress, on_delete=models.CASCADE)
#     user =  models.ForeignKey(User, on_delete=models.CASCADE)
#     rehv=   models.ForeignKey(heavyvehivalregistration,on_delete=models.SET_NULL,null=True)
#     status = models.BooleanField(default=False)
#     service_date = models.DateField()
#     is_active = models.BooleanField(default=True)
#     def __str__(self):
#         return self.user.mobile_number
    

#     class Meta:
#         db_table = "request_heavy_vehical"



# #############Sub contractor  registrations class #####################

# class subcontractorregistration(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE)

#     contractorname = models.CharField(max_length=100)
#     firmname = models.CharField(max_length=500)
#     typeofwork = models.CharField(max_length=100)
#     emailId = models.CharField(max_length=50)
#     expriencesinyear = models.IntegerField(blank=False, null=False)
#     license_number = models.CharField(max_length=50)
#     Aadharnumberfrontimage = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     Aadharnumberbackimage = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     mobilenumber = models.CharField(max_length=20)
#     subcontractor_image = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     subcontractor_image_back = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     subcontractor_image_left = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     subcontractor_image_right = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)

#     class Meta:
#         db_table = "subcontractorregistration"

# ############ subcontructor address #############

# class Sub_Contructoraddress(models.Model):
#     user_id = models.IntegerField(default=0)
#     subcontractorregistration = models.ForeignKey(subcontractorregistration, on_delete=models.CASCADE)
#     state_id = models.CharField(max_length=20)
#     district_id = models.CharField(max_length=20)
#     city_id = models.CharField(max_length=20)
#     is_active = models.BooleanField(default=1,null=False)
    

#     class Meta:
#         db_table = 'subcontructoraddress'

        

# class Request_SubContractor(models.Model):
#     Id = models.AutoField(primary_key=True, )
#     reqs=models.ForeignKey(subcontractorregistration,on_delete=models.SET_NULL,null=True)
#     userloginmobileno = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

#     contractorname = models.CharField(max_length=100)
#     firmname = models.CharField(max_length=500) 
#     typeofwork = models.CharField(max_length=100)
#     expriencesinyear = models.IntegerField(blank=False, null=False)
#     license_number = models.CharField(max_length=50)
#     emailId = models.CharField(max_length=100)
#     Aadharnumberfrontimage = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     Aadharnumberbackimage = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     mobilenumber = models.CharField(max_length=20)
#     subcontractor_image = models.TextField()
#     subcontractor_image_back = models.TextField()
#     subcontractor_image_left = models.TextField()
#     subcontractor_image_right = models.TextField()
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)
#     class Meta:
#         db_table = "request_subcontractor"
        
        
# class Requirement(models.Model):
#     Id = models.AutoField(primary_key=True, )
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     requirement_image = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)

#     class Meta:
#         db_table = "requirement"

# class RequestRequirement(models.Model):
#     Id = models.AutoField(primary_key=True, )
#     relqv = models.ForeignKey(Requirement, on_delete=models.SET_NULL,null=True)
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     requirement_image = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)
#     class Meta:
#         db_table = "request_requirement"
        
# class VedioUplaod(models.Model):
#     Id = models.AutoField(primary_key=True)
#     image_uplaod = models.CharField(max_length=500)
#     vediourl = models.CharField(max_length=100)
#     class Meta:
#         db_table = "vedioupload"


        
        
# ################# Request Api ###############


# class Request_labour_contructor(models.Model):
#     Id = models.AutoField(primary_key=True)
#     labreq = models.ForeignKey(labour_contructor,models.SET_NULL,null=True)
#     userloginmobileno = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

#     labourcontractorname = models.CharField(max_length=300)
#     labourwork = models.CharField(max_length=200)
#     emailId = models.CharField(max_length=100)
#     lobourinnumber = models.CharField(max_length=500)
#     mobile_number = models.CharField(max_length=12)
#     skilledlabour =  models.IntegerField(null=False,blank=False)
#     unskilledlabour = models.IntegerField(blank=False)
#     professionallabour = models.IntegerField(null=False)
#     Aadharnumberfrontimage = models.CharField(max_length=25)
#     alternativemobilenumber = models.CharField(max_length=15)
#     Aadharnumberbackimage = models.CharField(max_length=25)
#     labour_image = models.CharField(max_length=500)
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)
#     status = models.BooleanField(default=False)


#     class Meta:
#         db_table = 'request_labour_contructor'
        
# class Request_driver_Operator(models.Model):
#     Id = models.AutoField(primary_key=True, )
#     dre = models.ForeignKey(driveroperatorregistration, on_delete=models.CASCADE)
#     userloginmobileno = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


#     vehicalname = models.CharField(max_length=200)
#     expriencesinyear = models.IntegerField(blank=False, null=False)
#     driveroperatorname = models.CharField(max_length=200)
#     emailId = models.CharField(max_length=100)
#     heavy_license = models.CharField(max_length=50)
#     Aadharnumberfrontimage = models.CharField(max_length=25)
#     Aadharnumberbackimage = models.CharField(max_length=25)
#     mobilenumber = models.CharField(max_length=20)
#     alternet_mobilenumber = models.IntegerField()
#     license_image = models.CharField(max_length=50)
#     driver_image = models.CharField(max_length=500, blank=True, null=True)
#     license_image = models.CharField(max_length=500)
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)

#     class Meta:
#         db_table = "request_driver_operator"


# class insertrecordsp(models.Model):
#     id = models.AutoField(primary_key=True)
#     firstname = models.CharField(max_length=200)
#     lastname = models.CharField(max_length=200)
#     email = models.CharField(max_length=100)


#     class Meta:
#         db_table = "emptable"
        


# class test(models.Model):
#     name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to="static/Uploaded/UserProfiles/")
#     created_by =  models.IntegerField()
#     is_active = models.BooleanField(default=1,null=False)
#     class Meta:
#         db_table = "test"


# class discount_coupon(models.Model):
#     value = models.IntegerField()

# class user_coupon(models.Model):
#     user = models.ForeignKey(User ,  on_delete=models.CASCADE)
#     discount_coupon = models.ForeignKey(discount_coupon ,  on_delete=models.CASCADE)
#     expiry = models.DateField()

# class payment(models.Model):
#     user = models.ForeignKey(User ,  on_delete=models.CASCADE)  
#     razorpay_order_id =  models.CharField(max_length=100)
    
#     amount =  models.IntegerField()
#     discount = models.IntegerField(default=0)
#     heavyvehivalregistration = models.ForeignKey(heavyvehivalregistration ,  on_delete=models.CASCADE) 
#     status = models.BooleanField(default=False)

#     created_at      = models.DateTimeField(auto_now_add=True)
#     updated_at      = models.DateTimeField(auto_now=True)

    
    
class requirement(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    requirement_image = models.ImageField(upload_to="Requirement")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural =  "Requiremnt"
        db_table = 'requirement'

    def _str_(self):
        return str(self.title)
    
class accepted_requirement(models.Model):
    requirement = models.ForeignKey(requirement , on_delete=models.CASCADE , related_name="requested_requirement")
    user = models.ForeignKey(profileofall , on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural =  "Accepted Requiremnt"
        db_table = 'accepted_requirement'

    def _str_(self):
        return self.user.user.first_name +"==>"+ str(self.user.user.mobile_number)



