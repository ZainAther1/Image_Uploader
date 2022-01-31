from django.db import models
from datetime import datetime
from osgeo import gdal


# lists of options
cities_name_list=(("Abbotabad","Abbotabad"),("Bahawalpur","Bahawalpur"),("Charsaddah","Charsaddah"),("Dera Ghazi Khan","Dera Ghazi Khan"),("Faisalabad","Faisalabad"),("Gawadar","Gawadar"),("Islamabad","Islamabad"),("Rawalpindi","Rawalpindi"),("Karachi","Karachi"),("Lahore","Lahore"),("Multan","Multan"),("None","None"))
# massavi_sheets=(("Alif-1","Alif-1"),("Bay-1","Bay-1"),("Jeem-1","Jeem-1"),("Daal-1","Daal-1"),("Hay-1","Hay-1"),("Wao-1","Wao-1"),("None","None"))
massavi_sheets =(("Alif-1","Alif-1"),
("Alif-2","Alif-2"),
("Alif-3","Alif-3"),
("Alif-4","Alif-4"),
("Alif-5","Alif-5"),
("Alif-6","Alif-6"),
("Alif-7","Alif-7"),
("Alif-8","Alif-8"),
("Alif-9","Alif-9"),
("Alif-10","Alif-10"),
("Alif-11","Alif-11"),
("Alif-12","Alif-12"),
("Alif-13","Alif-13"),
("Alif-14","Alif-14"),
("Alif-15","Alif-15"),
("Alif-16","Alif-16"),
("Bay-1","Bay-1"),
("Bay-2","Bay-2"),
("Bay-3","Bay-3"),
("Bay-4","Bay-4"),
("Bay-5","Bay-5"),
("Bay-6","Bay-6"),
("Bay-7","Bay-7"),
("Bay-8","Bay-8"),
("Bay-9","Bay-9"),
("Bay-10","Bay-10"),
("Bay-11","Bay-11"),
("Bay-12","Bay-12"),
("Bay-13","Bay-13"),
("Bay-14","Bay-14"),
("Bay-15","Bay-15"),
("Bay-16","Bay-16"),
("Jeem-1","Jeem-1"),
("Jeem-2","Jeem-2"),
("Jeem-3","Jeem-3"),
("Jeem-4","Jeem-4"),
("Jeem-5","Jeem-5"),
("Jeem-6","Jeem-6"),
("Jeem-7","Jeem-7"),
("Jeem-8","Jeem-8"),
("Jeem-9","Jeem-9"),
("Jeem-10","Jeem-10"),
("Jeem-11","Jeem-11"),
("Jeem-12","Jeem-12"),
("Jeem-13","Jeem-13"),
("Jeem-14","Jeem-14"),
("Jeem-15","Jeem-15"),
("Jeem-16","Jeem-16"),
("Daal-1","Daal-1"),
("Daal-2","Daal-2"),
("Daal-3","Daal-3"),
("Daal-4","Daal-4"),
("Daal-5","Daal-5"),
("Daal-6","Daal-6"),
("Daal-7","Daal-7"),
("Daal-8","Daal-8"),
("Daal-9","Daal-9"),
("Daal-10","Daal-10"),
("Daal-11","Daal-11"),
("Daal-12","Daal-12"),
("Daal-13","Daal-13"),
("Daal-14","Daal-14"),
("Daal-15","Daal-15"),
("Daal-16","Daal-16"),
("Hay-1","Hay-1"),
("Hay-2","Hay-2"),
("Hay-3","Hay-3"),
("Hay-4","Hay-4"),
("Hay-5","Hay-5"),
("Hay-6","Hay-6"),
("Hay-7","Hay-7"),
("Hay-8","Hay-8"),
("Hay-9","Hay-9"),
("Hay-10","Hay-10"),
("Hay-11","Hay-11"),
("Hay-12","Hay-12"),
("Hay-13","Hay-13"),
("Hay-14","Hay-14"),
("Hay-15","Hay-15"),
("Hay-16","Hay-16"),
("Wao-1","Wao-1"),
("Wao-2","Wao-2"),
("Wao-3","Wao-3"),
("Wao-4","Wao-4"),
("Wao-5","Wao-5"),
("Wao-6","Wao-6"),
("Wao-7","Wao-7"),
("Wao-8","Wao-8"),
("Wao-9","Wao-9"),
("Wao-10","Wao-10"),
("Wao-11","Wao-11"),
("Wao-12","Wao-12"),
("Wao-13","Wao-13"),
("Wao-14","Wao-14"),
("Wao-15","Wao-15"),
("Wao-16","Wao-16"),
("Zay-1","Zay-1"),
("Zay-2","Zay-2"),
("Zay-3","Zay-3"),
("Zay-4","Zay-4"),
("Zay-5","Zay-5"),
("Zay-6","Zay-6"),
("Zay-7","Zay-7"),
("Zay-8","Zay-8"),
("Zay-9","Zay-9"),
("Zay-10","Zay-10"),
("Zay-11","Zay-11"),
("Zay-12","Zay-12"),
("Zay-13","Zay-13"),
("Zay-14","Zay-14"),
("Zay-15","Zay-15"),
("Zay-16","Zay-16"),
("Tuayn-1","Tuayn-1"),
("Tuayn-2","Tuayn-2"),
("Tuayn-3","Tuayn-3"),
("Tuayn-4","Tuayn-4"),
("Tuayn-5","Tuayn-5"),
("Tuayn-6","Tuayn-6"),
("Tuayn-7","Tuayn-7"),
("Tuayn-8","Tuayn-8"),
("Tuayn-9","Tuayn-9"),
("Tuayn-10","Tuayn-10"),
("Tuayn-11","Tuayn-11"),
("Tuayn-12","Tuayn-12"),
("Tuayn-13","Tuayn-13"),
("Tuayn-14","Tuayn-14"),
("Tuayn-15","Tuayn-15"),
("Tuayn-16","Tuayn-16"),
("Yay-1","Yay-1"),
("Yay-2","Yay-2"),
("Yay-3","Yay-3"),
("Yay-4","Yay-4"),
("Yay-5","Yay-5"),
("Yay-6","Yay-6"),
("Yay-7","Yay-7"),
("Yay-8","Yay-8"),
("Yay-9","Yay-9"),
("Yay-10","Yay-10"),
("Yay-11","Yay-11"),
("Yay-12","Yay-12"),
("Yay-13","Yay-13"),
("Yay-14","Yay-14"),
("Yay-15","Yay-15"),
("Yay-16","Yay-16"),
("Kaaf-1","Kaaf-1"),
("Kaaf-2","Kaaf-2"),
("Kaaf-3","Kaaf-3"),
("Kaaf-4","Kaaf-4"),
("Kaaf-5","Kaaf-5"),
("Kaaf-6","Kaaf-6"),
("Kaaf-7","Kaaf-7"),
("Kaaf-8","Kaaf-8"),
("Kaaf-9","Kaaf-9"),
("Kaaf-10","Kaaf-10"),
("Kaaf-11","Kaaf-11"),
("Kaaf-12","Kaaf-12"),
("Kaaf-13","Kaaf-13"),
("Kaaf-14","Kaaf-14"),
("Kaaf-15","Kaaf-15"),
("Kaaf-16","Kaaf-16"),
("Laam-1","Laam-1"),
("Laam-2","Laam-2"),
("Laam-3","Laam-3"),
("Laam-4","Laam-4"),
("Laam-5","Laam-5"),
("Laam-6","Laam-6"),
("Laam-7","Laam-7"),
("Laam-8","Laam-8"),
("Laam-9","Laam-9"),
("Laam-10","Laam-10"),
("Laam-11","Laam-11"),
("Laam-12","Laam-12"),
("Laam-13","Laam-13"),
("Laam-14","Laam-14"),
("Laam-15","Laam-15"),
("Laam-16","Laam-16"),
("Meem-1","Meem-1"),
("Meem-2","Meem-2"),
("Meem-3","Meem-3"),
("Meem-4","Meem-4"),
("Meem-5","Meem-5"),
("Meem-6","Meem-6"),
("Meem-7","Meem-7"),
("Meem-8","Meem-8"),
("Meem-9","Meem-9"),
("Meem-10","Meem-10"),
("Meem-11","Meem-11"),
("Meem-12","Meem-12"),
("Meem-13","Meem-13"),
("Meem-14","Meem-14"),
("Meem-15","Meem-15"),
("Meem-16","Meem-16"),
("Noon-1","Noon-1"),
("Noon-2","Noon-2"),
("Noon-3","Noon-3"),
("Noon-4","Noon-4"),
("Noon-5","Noon-5"),
("Noon-6","Noon-6"),
("Noon-7","Noon-7"),
("Noon-8","Noon-8"),
("Noon-9","Noon-9"),
("Noon-10","Noon-10"),
("Noon-11","Noon-11"),
("Noon-12","Noon-12"),
("Noon-13","Noon-13"),
("Noon-14","Noon-14"),
("Noon-15","Noon-15"),
("Noon-16","Noon-16"),
("Seen-1","Seen-1"),
("Seen-2","Seen-2"),
("Seen-3","Seen-3"),
("Seen-4","Seen-4"),
("Seen-5","Seen-5"),
("Seen-6","Seen-6"),
("Seen-7","Seen-7"),
("Seen-8","Seen-8"),
("Seen-9","Seen-9"),
("Seen-10","Seen-10"),
("Seen-11","Seen-11"),
("Seen-12","Seen-12"),
("Seen-13","Seen-13"),
("Seen-14","Seen-14"),
("Seen-15","Seen-15"),
("Seen-16","Seen-16"),
("Ayn-1","Ayn-1"),
("Ayn-2","Ayn-2"),
("Ayn-3","Ayn-3"),
("Ayn-4","Ayn-4"),
("Ayn-5","Ayn-5"),
("Ayn-6","Ayn-6"),
("Ayn-7","Ayn-7"),
("Ayn-8","Ayn-8"),
("Ayn-9","Ayn-9"),
("Ayn-10","Ayn-10"),
("Ayn-11","Ayn-11"),
("Ayn-12","Ayn-12"),
("Ayn-13","Ayn-13"),
("Ayn-14","Ayn-14"),
("Ayn-15","Ayn-15"),
("Ayn-16","Ayn-16"),
("Fay-1","Fay-1"),
("Fay-2","Fay-2"),
("Fay-3","Fay-3"),
("Fay-4","Fay-4"),
("Fay-5","Fay-5"),
("Fay-6","Fay-6"),
("Fay-7","Fay-7"),
("Fay-8","Fay-8"),
("Fay-9","Fay-9"),
("Fay-10","Fay-10"),
("Fay-11","Fay-11"),
("Fay-12","Fay-12"),
("Fay-13","Fay-13"),
("Fay-14","Fay-14"),
("Fay-15","Fay-15"),
("Fay-16","Fay-16"),
("Suaad-1","Suaad-1"),
("Suaad-2","Suaad-2"),
("Suaad-3","Suaad-3"),
("Suaad-4","Suaad-4"),
("Suaad-5","Suaad-5"),
("Suaad-6","Suaad-6"),
("Suaad-7","Suaad-7"),
("Suaad-8","Suaad-8"),
("Suaad-9","Suaad-9"),
("Suaad-10","Suaad-10"),
("Suaad-11","Suaad-11"),
("Suaad-12","Suaad-12"),
("Suaad-13","Suaad-13"),
("Suaad-14","Suaad-14"),
("Suaad-15","Suaad-15"),
("Suaad-16","Suaad-16"),
("Qaaf-1","Qaaf-1"),
("Qaaf-2","Qaaf-2"),
("Qaaf-3","Qaaf-3"),
("Qaaf-4","Qaaf-4"),
("Qaaf-5","Qaaf-5"),
("Qaaf-6","Qaaf-6"),
("Qaaf-7","Qaaf-7"),
("Qaaf-8","Qaaf-8"),
("Qaaf-9","Qaaf-9"),
("Qaaf-10","Qaaf-10"),
("Qaaf-11","Qaaf-11"),
("Qaaf-12","Qaaf-12"),
("Qaaf-13","Qaaf-13"),
("Qaaf-14","Qaaf-14"),
("Qaaf-15","Qaaf-15"),
("Qaaf-16","Qaaf-16"),
("Ray-1","Ray-1"),
("Ray-2","Ray-2"),
("Ray-3","Ray-3"),
("Ray-4","Ray-4"),
("Ray-5","Ray-5"),
("Ray-6","Ray-6"),
("Ray-7","Ray-7"),
("Ray-8","Ray-8"),
("Ray-9","Ray-9"),
("Ray-10","Ray-10"),
("Ray-11","Ray-11"),
("Ray-12","Ray-12"),
("Ray-13","Ray-13"),
("Ray-14","Ray-14"),
("Ray-15","Ray-15"),
("Ray-16","Ray-16"))




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
    
    

    
    
