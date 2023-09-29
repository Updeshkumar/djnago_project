from .models import *
from django import forms



class AddLabourForm(forms.ModelForm):
    class Meta:
        model = labour_contructor
        exclude = ('user', 'expired_at','labour_paid' ,'is_active')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'labourwork':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'emailId':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'lobourinnumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'skilledlabour':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'unskilledlabour':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'professionallabour':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'Aadharnumberfrontimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'Aadharnumberbackimage':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'alternativemobilenumber':forms.TextInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),
            'labour_image':forms.FileInput(attrs={'class':'form-control mb-3' , 'placeholder':''}),         
        }

        