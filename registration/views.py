from django.shortcuts import redirect, render
from registration.forms import Registration
from django.contrib import messages

# Create your views here.
def registerHome(request):
    if request.method == 'GET':
        form  = Registration()
        context = {'form': form}
        return render(request, 'Register/userRegister.html', context)
    if request.method == 'POST':
        form  = Registration(request.POST)
        if form.is_valid():
            try:
                form.save()
                user = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login:userLogin')
            except:
                messages.error(request, 'User Exist')
                context = {'form': Registration()}
                return render(request, 'Register/userRegister.html', context)
        else:
            messages.error(request, 'Form is not valid')
            context = {'form': form}
            return render(request, 'Register/userRegister.html', context)
    return render(request, 'Register/userRegister.html', {})