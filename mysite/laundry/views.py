from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages, auth
from django.contrib.auth import authenticate

# Create your views here.

@csrf_protect
def get_authenticate(request):
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        auth.login(request,user)
        return dashboard(request)
    else:
        messages.info(request, 'Invalid Username or Password')
        return redirect('login')

def login(request):
    return render(request, 'login.html')
    
@csrf_protect
def dashboard(request):
    if request.user.is_authenticated:
        rent_details = None
        return render(request, 'dashboard.html')
    else:
        messages.info(request, 'Please login .. !')
        return render(request, 'login.html')