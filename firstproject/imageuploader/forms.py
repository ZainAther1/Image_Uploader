from django.db import models  
from django.forms import fields  
from .models import UploadImage 
from .models import cities_list
from .models import Geeks_Model

from django import forms  
  

# iterable
GEEKS_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


# creating a form 
class GeeksForm(forms.ModelForm):
    class Meta:
        model = Geeks_Model
    
        name = forms.ChoiceField(choices = GEEKS_CHOICES)
        age = forms.ChoiceField(choices = GEEKS_CHOICES)
        
        fields = '__all__'
    
    
 
 
 
  
class UserImageForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImage  
        # It includes all the fields of model  
        fields = '__all__'

        
        
 
