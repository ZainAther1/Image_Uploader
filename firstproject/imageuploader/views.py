from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render  
from imageuploader.forms import UserImageForm  
from .models import UploadImage  

from django.views.generic import ListView
from imageuploader.models import UploadImage
  

from django.core.paginator import Paginator

  
from .models import UploadImage


from django.db import IntegrityError
from django.http import HttpResponse

from .filters import UploadImageFilter
from django.contrib import messages


  

  
  
def index(request):
    return render(request, 'index.html') 

def error(request):
    return render(request, 'error.html')

# def create(request):
#     if request.method == 'POST':
        
#         form_id = request.POST.get('form_id')
#         image = request.POST.get('image')
#         type_data = request.POST.get('type_data')
#         district = request.POST.get('district')
#         tehsil = request.POST.get('tehsil')
#         patwar_circle = request.POST.get('patwar_circle')
#         mauza = request.POST.get('mauza')
#         massavi_no = request.POST.get('massavi_no')
        
#         new_profile = UploadImage(form_id=form_id, image=image, type_data=type_data, district=district, tehsil=tehsil, patwar_circle=patwar_circle, mauza=mauza, massavi_no=massavi_no)
        
#         new_profile.save()
        
#         success = 'Form Submitted Successfully'
#         return HttpResponse(success)
    
    
    
        
        
  
  
def image_request(request):  
    
    
        if request.method == 'POST':  
            try:
                form = UserImageForm(request.POST, request.FILES)  
                if form.is_valid():  
                
                    form.save()  
  
                    # Getting the current instance object to display in the template  
                    img_object = form.instance  
              
                    return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  

                else:
                    # print("form.errors:", form.errors)
                    success = 'Form Submission'
                    return HttpResponse(success)               
            
            except IntegrityError:
                  
                    return render(request, 'image_form.html', {'form': form,'message':' '})
                    # return HttpResponse('<h1 style="color: red;">Form already exists</h1>')        
        
        else:  
            form = UserImageForm()  
  
        return render(request, 'image_form.html', {'form': form})  




def search(request):
    
    search_query = request.GET.get('search',None)
    
    
    if search_query:
        posts = UploadImage.objects.filter(Q(form_id__icontains = search_query))
        
    
    else:
        posts = UploadImage.objects.all()
    
    
    return render(request, 'search_results.html')
    
    # """ search function  """
    # if request.method == "GET":
    #     query_name = request.GET.get('search', None)
    #     if query_name:
    #         results = UploadImage.objects.filter(desc__contains=query_name)
    #         return render(request, 'search_results.html', {"results":results})

    # return render(request, 'search_results.html')



# def error(request):
#     return render(request, 'Error.html')


# to have a list view of images
# class Images_List(ListView):
    
#     template_name = 'uploadimage_list.html'
#     # number of items per page
#     paginate_by = 2

#     model = UploadImage
    
# def Images_List(request):
    
#     model = UploadImage
    
#     template_name = 'uploadimage_list.html'
    
#     # number of items per page
#     paginate_by = 2
    
#     queryset = UploadImage.objects.all()
    
#     myFilter = UploadImageFilter()
    
#     context = {'queryset': queryset, 'myFilter': myFilter}
    
    
#     return render(request,'imageuploader/uploadimage_list.html', context)    
    
    
def Images_List(request):
    context ={}
    
    filtered_images = UploadImageFilter(
        
        request.GET,
        queryset = UploadImage.objects.all(),
        
    )
    
    context['filtered_images'] = filtered_images
    
    paginated_filtered_entries = Paginator(filtered_images.qs, 20)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_entries.get_page(page_number)
    

    
    context['person_page_obj'] = person_page_obj
    
    return render(request,'imageuploader/uploadimage_list.html', context=context)


    
    
    







