from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import bankRequest
# Create your views here.

class loginView(LoginView):
    template_name='Login/userLogin.html'
    next_page='login:userHome'

@login_required(login_url='login:userLogin')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def userHome(request):
   return render(request,'serviceFrame/userHome.html')
    

class signout(LogoutView):
    next_page='home:home'

@login_required(login_url='login:userLogin')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def requestBlood(request):
    context={}
    form=bankRequest(request.POST)
    context['form']=form
    if request.method=='POST':
       if form.is_valid():
           req=form.save()
           messages.success(request,'Request Submitted:'+req.pk)
           return redirect('login:b_request')
       else:
            messages.error(request,'Form Invalid')
    return render(request,'serviceFrame/bloodBank.html',context)

