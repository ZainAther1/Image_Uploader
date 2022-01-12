from django.contrib import admin

from imageuploader.models import UploadImage

from imageuploader.models import cities_list

from imageuploader.models import Geeks_Model

# Register your models here.

admin.site.register(UploadImage)
admin.site.register(cities_list)
admin.site.register(Geeks_Model)