from .models import *
from django import forms



class AddSubcontructorForm(forms.ModelForm):
    class Meta:
        model = subcontractorregistration
        exclude = ('user', 'expired_at','subcontructor_paid' ,'is_active')

        widgets = {
            'contractorname':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'firmname':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'typeofwork':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'emailId':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'expriencesinyear':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'license_number':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'mobilenumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'subcontractor_image':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'subcontractor_image_back':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'subcontractor_image_left':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'subcontractor_image_right':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),

            'Aadharnumberfrontimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'Aadharnumberbackimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
        }
        