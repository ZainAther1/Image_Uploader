from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render  
from imageuploader.forms import UserImageForm  
from .models import UploadImage  

from django.views.generic import ListView
from imageuploader.models import UploadImage
  

from django.db.models import Q

  
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




def search(request):
    
    search_query = request.GET.get('search',None)
    
    
    if search_query:
        posts = UploadImage.objects.filter(Q(desc__icontains = search_query))
        
    
    else:
        posts = UploadImage.objects.all
    
    
    return render(request, 'search_results.html')
    
    # """ search function  """
    # if request.method == "GET":
    #     query_name = request.GET.get('search', None)
    #     if query_name:
    #         results = UploadImage.objects.filter(desc__contains=query_name)
    #         return render(request, 'search_results.html', {"results":results})

    # return render(request, 'search_results.html')




# to have a list view of images
class Images_List(ListView):
    
    
    model = UploadImage
    
    
    
class SearchResultsView(ListView):
    model = UploadImage
    template_name = 'search_results.html'