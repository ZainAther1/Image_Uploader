from django.db import models



# Create your models here.
class UploadImage(models.Model):  
    
    image_id = models.CharField(max_length=20, primary_key=True, unique=True, default=1)
    desc = models.TextField(max_length=20, null=True, blank=True)  
    image = models.ImageField(upload_to='images', null=True, blank=True)  
  
    def __str__(self):  
        return self.image_id  
    
    
    
