from django.urls import path
from .views import about, index
app_name='home'
urlpatterns=[
    path('',index,name='home'),
    path('about',about,name='about'),
]