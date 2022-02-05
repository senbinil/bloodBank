from django.urls import path
from .views import registerHome

app_name='register'
urlpatterns = [
    path('',registerHome,name='userRegister'),
]
