from django.urls import path  
from .views import image_request  
from . import views


from imageuploader.views import Images_List


from imageuploader.views import SearchResultsView


app_name = 'imageuploader'  
urlpatterns = [  
    path('', views.index, name = "Home"),
    path('add/', views.image_request, name='upload'),
    path ('list/', Images_List.as_view(), name='list'),
    path('search/', views.search, name='search_results'),
    path('cities/', views.cities_view, name='cities_names'),
    path('home/', views.home_view ),
    ]

# SearchResultsView.as_view()