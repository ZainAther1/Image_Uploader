from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render  
from imageuploader.forms import UserImageForm  
from .models import UploadImage  

from django.views.generic import ListView
from imageuploader.models import UploadImage
  

from django.db.models import Q

  
from .models import UploadImage
from .models import cities_list



from .forms import GeeksForm

  

  
  
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
    
    
    
cities_name=['Abbotabad','Bahawalpur','Charsaddah','Dera Ghazi Khan','Faisalabad','Gawadar','Islamabad','Rawalpindi','Karachi','Faislabad','Lahore','Multan']
    
def cities_view(request, *args, **kwargs):
    
        # Iterate through all the data items
    for i in range(len(cities_name)):

        # Insert in the database
        cities_list.objects.create(cities = cities_name[i])


    # Getting all the stuff from database
    query_results = cities_list.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }

    # Returning the rendered html
    return render(request, "cities.html", context)







# Create your views here.
def home_view(request):
    context = {}
    context['form'] = GeeksForm()
    
    
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'home.html', {'form': form, 'img_obj': img_object})  
        
        
    else:  
        form = UserImageForm()  
  
    return render(request, 'home.html', {'form': form}, context)
    # return render( request, "home.html", context)