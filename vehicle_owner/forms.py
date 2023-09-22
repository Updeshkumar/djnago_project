from .models import *
from django import forms



class AddHeavyVehile(forms.ModelForm):
    class Meta:
        model = heavyvehivalregistration
        exclude = ('user', 'expired_at','is_paid', 'is_active')

        widgets = {
            'vehical_name':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'company_name':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'emailId':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'ownername':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'vehicleregistrationnumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            
            
            'Aadharnumberfrontimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'Aadharnumberbackimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            
            
            'vehicle_image':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'vehicle_image_back':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'vehicle_image_left':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'vehicle_image_right':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            
            
            'manufacture_date':forms.DateInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'alternativemobilenumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'vehiclemodelnumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
        }

        