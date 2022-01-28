import django_filters
from django_filters import DateFilter

from .models import *

class UploadImageFilter(django_filters.FilterSet):
    class Meta:
        model = UploadImage
        fields = '__all__'
        time_now = DateFilter (field_name='time_now', lookup_expr='icontains')
        exclude = ['image','form_id','type_data']