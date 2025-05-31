from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def admin_login(request):
    try:
        logout(request)
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = username)
            if not user_obj.exists():
                messages.info(request, 'User does not exist')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username = username, password = password)
            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('dashboard')

            messages.info(request, 'Invalid credentials')
            return redirect('adminlogin')

        return render(request, 'admin-login.html')
    
    except Exception as e:
        print(e)
        return HttpResponse("An error occurred: {}".format(e), status=500)
    
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'admin-dashboard.html')
        else:
            messages.info(request, 'You are not authorized to access this page')
            return redirect('adminlogin')
    else:
        messages.info(request, 'You are not logged in')
        return redirect('adminlogin')