from django.db import models


# lists of options
cities_name_list=(("Abbotabad","Abbotabad"),("Bahawalpur","Bahawalpur"),("Charsaddah","Charsaddah"),("Dera Ghazi Khan","Dera Ghazi Khan"),("Faisalabad","Faisalabad"),("Gawadar","Gawadar"),("Islamabad","Islamabad"),("Rawalpindi","Rawalpindi"),("Karachi","Karachi"),("Faislabad","Faislabad"),("Lahore","Lahore"),("Multan","Multan"))
massavi_sheets=(("Alif-1","Alif-1"),("Bay-1","Bay-1"),("Jeem-1","Jeem-1"),("Daal-1","Daal-1"),("Hay-1","Hay-1"),("Wao-1","Wao-1"))






# Create your models here.
class UploadImage(models.Model):  
    
    form_id = models.CharField(max_length=20, primary_key=True, unique=True, default=1) 
    
    image = models.ImageField(upload_to='images', null=True, blank=True)  
    
    type_data = models.CharField(max_length=50, null=True, blank=True, default="Massavi")
    
    district = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    tehsil = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    patwar_circle = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    mauza = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    massavi_no = models.CharField(max_length=50, null=True, blank=True,choices = massavi_sheets)
    
    
    
  
  
  
    def __str__(self):  
        return self.form_id  
    
    
    
class cities_list(models.Model):
    # newly added
    cities = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):  
        return self.cities 
    
    
    
    
class Geeks_Model(models.Model):
    
    name = models.CharField(max_length=50, null=True, blank=True)
    
    age = models.CharField(max_length=50, null=True, blank=True)
    
    
