from django.db import models



# Create your models here.
class UploadImage(models.Model):  
    
    form_id = models.CharField(max_length=20, primary_key=True, unique=True, default=1) 
    
    image = models.ImageField(upload_to='images', null=True, blank=True)  
    
    type_data = models.CharField(max_length=50, null=True, blank=True)
    
    district = models.CharField(max_length=50, null=True, blank=True)
    
    tehsil = models.CharField(max_length=50, null=True, blank=True)
    
    patwar_circle = models.CharField(max_length=50, null=True, blank=True)
    
    mauza = models.CharField(max_length=50, null=True, blank=True)
    
    massavi_no = models.CharField(max_length=50, null=True, blank=True)
  
  
  
    def __str__(self):  
        return self.form_id  
    
    
    
