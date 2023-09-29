from .models import *
from django import forms



class AddDriverForm(forms.ModelForm):
    class Meta:
        model = driver_profile
        exclude = ('user', 'expired_at','driver_paid' ,'is_active')

        widgets = {
            'vehicalname':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'expriencesinyear':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'driveroperatorname':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'Aadharnumberfrontimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'Aadharnumberbackimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'alternet_mobilenumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'heavy_license':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'emailId':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'mobilenumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'license_image':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'driver_image':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),         
        }

        