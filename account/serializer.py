from all_import.all_import import *


class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model = state
        fields = '__all__'


class districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = district
        fields = '__all__'


class tahseelSerializer(serializers.ModelSerializer):
    class Meta:
        model = tahseel
        fields = '__all__'





## Heavy vehicle 
class VehicleUserAddress(serializers.ModelSerializer):
    class Meta:
        model = heavyvehicleaddress
        exclude = ("user", )
        depth = 1



class AllHeavyVehicle(serializers.ModelSerializer):
    address     = serializers.SerializerMethodField()
    is_reserved = serializers.SerializerMethodField()
    my_request  = serializers.SerializerMethodField()
    
    def get_address(self, obj):
        getAd=heavyvehicleaddress.objects.filter(user=obj.user).first()
        ser=VehicleUserAddress(getAd , many=False)
        return ser.data
    
    def get_is_reserved(self,obj):
        if request_vehicle.objects.filter(heavyvehivalregistration=obj , reserved=True).exists():
            res=True
        else:
            res = False
        return res        
    
    def get_my_request(self , obj):
        if request_vehicle.objects.filter(heavyvehivalregistration=obj).exists():
            req=True 
        else:
            req = False
        return req    
    
    
    class Meta:
        model   = heavyvehivalregistration
        fields = (
                "id",
                "user",
                "vehical_name",
                "company_name",
                "emailId",
                "ownername",
                "vehicleregistrationnumber",
                "Aadharnumberfrontimage" ,
                "Aadharnumberbackimage",
                "vehicle_image",
                "vehicle_image_back",
                "vehicle_image_left",
                "vehicle_image_right",
                "manufacture_date",
                "alternativemobilenumber",
                "vehiclemodelnumber",
                "is_active", 
                "expired_at",
                "is_reserved",                
                "address" ,
                "my_request"  
        )



# Driver 
class DriverAddress(serializers.ModelSerializer):
    class Meta:
        model = driver_Address
        exclude = ("user", )
        depth = 1


class GETDriver(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    is_reserved = serializers.SerializerMethodField()
    my_request = serializers.SerializerMethodField()
    
    def get_address(self, obj):
        getAd=driver_Address.objects.filter(user=obj).first()
        ser=DriverAddress(getAd , many=False)
        return ser.data
    def get_is_reserved(self,obj):
        if request_driver.objects.filter(driver_profile=obj , reserved=True).exists():
            res=True
        else:
            res = False
        return res        
    def get_my_request(self , obj):
        if request_driver.objects.filter(driver_profile=obj).exists():
            req=True 
        else:
            req = False
        return req    
    
    
    class Meta:
        model = driver_profile
        fields=(
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
            "driver_paid",
            "expired_at",
            "address",
            "is_reserved",
            "my_request",
        )
        


# Labour
class LabourAddress(serializers.ModelSerializer):
    class Meta:
        model = labour_address
        exclude = ("user", )
        depth = 1


class LabourProfile(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    is_reserved = serializers.SerializerMethodField()
    my_request = serializers.SerializerMethodField()
    
    def get_address(self, obj):
        getAd=labour_address.objects.filter(user=obj).first()
        ser=LabourAddress(getAd , many=False)
        return ser.data
    

    
    def get_is_reserved(self,obj):
        if request_labour.objects.filter(labour_contructor=obj , reserved=True).exists():
            res=True
        else:
            res = False
        return res        
    def get_my_request(self , obj):
        if request_labour.objects.filter(labour_contructor=obj).exists():
            req=True 
        else:
            req = False
        return req        

    
    class Meta:
        model   = labour_contructor
        fields = (
            "id",
            "user",
            "name",
            "labourwork",
            "emailId",
            "lobourinnumber",
            "mobile_number",
            "skilledlabour",
            "unskilledlabour",
            "professionallabour",
            "Aadharnumberfrontimage",
            "Aadharnumberbackimage",
            "alternativemobilenumber",
            "labour_image",
            "labour_paid",
            "expired_at",
            "is_active",
            "address",
            "is_reserved",
            "my_request",
        )


#### Sub contructor
class SubcontructorAddress(serializers.ModelSerializer):
    class Meta:
        model = subcontructor_Address
        exclude = ("user",)
        depth = 1
        

class SubContructorProfile(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    is_reserved = serializers.SerializerMethodField()
    my_request = serializers.SerializerMethodField()
    
    def get_address(self, obj):
        getAd=subcontructor_Address.objects.filter(user=obj).first()
        ser=SubcontructorAddress(getAd , many=False)
        return ser.data
    

    
    def get_is_reserved(self,obj):
        if request_subcontructor.objects.filter(subcontractorregistration=obj , reserved=True).exists():
            res=True
        else:
            res = False
        return res        
    def get_my_request(self , obj):
        if request_subcontructor.objects.filter(subcontractorregistration=obj).exists():
            req=True 
        else:
            req = False
        return req        

    
    class Meta:
        model   = subcontractorregistration
        fields = (
            "id",
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
            "expired_at",
            "is_active",
            "address",
            "is_reserved",
            "my_request",
        )

# requiremnts serializers

class AcceptedRequirement(serializers.ModelSerializer):
    class Meta:
        model = accepted_requirement
        exclude = ("user", )


class RequremntSerializer(serializers.ModelSerializer):
    accepted_requirement  = serializers.SerializerMethodField()

    def get_accepted_requirement(self , obj):
        get_obj=accepted_requirement.objects.filter(requirement=obj).first()
        s=AcceptedRequirement(get_obj , many=False)
        return s.data
    
    class Meta:
        model = requirement 
        fields = '__all__'

class AddRequiremnt(serializers.ModelSerializer):  
    class Meta:
        model = accepted_requirement 
        exclude = ('user',)      




        
        


