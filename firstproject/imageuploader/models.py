from django.db import models
from django.db import IntegrityError
from django.http import HttpResponse
from datetime import datetime



# lists of options
cities_name_list=(("Abbotabad","Abbotabad"),("Bahawalpur","Bahawalpur"),("Charsaddah","Charsaddah"),("Dera Ghazi Khan","Dera Ghazi Khan"),("Faisalabad","Faisalabad"),("Gawadar","Gawadar"),("Islamabad","Islamabad"),("Rawalpindi","Rawalpindi"),("Karachi","Karachi"),("Lahore","Lahore"),("Multan","Multan"),("None","None"))
massavi_sheets=(("Alif-1","Alif-1"),("Bay-1","Bay-1"),("Jeem-1","Jeem-1"),("Daal-1","Daal-1"),("Hay-1","Hay-1"),("Wao-1","Wao-1"),("None","None"))




# define upload path function
def content_file_name(instance, filename):
    name, ext = filename.split('.')
    file_path = 'images/{mauza}/{form_id}.{ext}'.format(
          form_id=instance.form_id, mauza=instance.mauza, ext=ext) 
    return file_path


# Create your models here.
class UploadImage(models.Model):  
    
    form_id = models.CharField(max_length=100, primary_key=True, unique=True, default=1) 
    
    time_now = models.DateField(default=datetime.now,blank=True)
    
    image = models.ImageField(max_length=200,upload_to= content_file_name, null=True, blank=True)  
    
    type_data = models.CharField(max_length=50, null=True, blank=True, default="Massavi")
    
    district = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    tehsil = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    patwar_circle = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    mauza = models.CharField(max_length=50, null=True, blank=True, choices = cities_name_list)
    
    massavi_no = models.CharField(max_length=50, null=True, blank=True,choices = massavi_sheets)
    
    
    
    
    def __str__(self):  
        return self.form_id 
  
  
    def save(self, *args, **kwargs):
        
        self.form_id = f'{self.district}_{self.tehsil}_{self.patwar_circle}_{self.mauza}_{self.massavi_no}'
        super(UploadImage,self).save(*args, **kwargs)
         
        
        # if IntegrityError:
        #         return HttpResponse("ERROR: form already exists!")
        
        
        
        # student=UploadImage.objects.get(pk=form_id)
        # student.save()
        # print (student.form_id)
    
    
    
    # def get_formid_value():
    
    #     formid_value = UploadImage.objects.get(pk=form_id)
    #     print(formid_value)
    #     return formid_value
    
    # my_object = get_formid_value()
    
    

    
    
