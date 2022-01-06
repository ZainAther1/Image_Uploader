from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render  
from imageuploader.forms import UserImageForm  
from .models import UploadImage  

from django.views.generic import ListView
from imageuploader.models import UploadImage
  
  
from .models import UploadImage
  






  
  
def index(request):
    return render(request, 'index.html')  
  
  
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
        
        
    else:  
        form = UserImageForm()  
  
    return render(request, 'image_form.html', {'form': form})  





# to have a list view of images
class Images_List(ListView):
    
    
    model = UploadImage
    
    
    
class SearchResultsView(ListView):
    model = UploadImage
    template_name = 'search_results.html'