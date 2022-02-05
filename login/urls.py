from django.urls import path
from .views import loginView, requestBlood,userHome,signout

app_name='login'
urlpatterns = [
    path('',loginView.as_view(),name='userLogin'),
    path('userHome/',userHome,name='userHome'),
    path('bloodRequest/',requestBlood,name='b_request'),
    path('logout',signout.as_view(),name='logout'),
]
