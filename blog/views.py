from django.shortcuts import render, redirect, get_object_or_404
from .models import Create, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def base(request):
    blogs = Create.objects.all().order_by('-date')
    return render(request, 'content.html', {'blogs': blogs, 'user': request.user})

def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            create = Create()
            create.title = request.POST.get('btitle')
            create.content = request.POST.get('bcontent')
            create.user = request.user
            create.save()
            return redirect('base')
            messages.success(request, 'Blog Posted successfully')
        return render(request, 'create.html')
    else:
        messages.error(request, '⚠️ User must be Logged-in')
        return redirect('login')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()
    return render(request, 'contact.html')

def showPage(request,slug):
    blog = get_object_or_404(Create, slug=slug)
    return render(request, 'page.html', {'blog':blog})

def about(request):
    return render(request, 'about.html')

def user_signup(request):
    return render(request, 'signup.html')

def user_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('base')
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username = username)
            if not user_obj.exists():
                messages.error(request, '⚠️ User does not exist')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username = username, password = password)
            if user_obj:
                messages.success(request, '✅ Logged in successfully')
                login(request, user_obj)
                return redirect('base')

            messages.error(request, 'Invalid credentials')
            return redirect('login')

        return render(request, 'login.html')
    
    except Exception as e:
        print(e)
        return HttpResponse("An error occurred: {}".format(e), status=500)
    
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('base')

def user_signup(request):
    if request.method == "POST":
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        if password != confirm_password:
            messages.info(request, '⚠️ Passwords do not match')
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username is already taken. Please choose a different one.")
            return redirect('signup')
        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, '✅ User created successfully')
        return redirect('login')
    return render(request, 'signup.html')


def user_profile(request):
    if request.user.is_authenticated:
        user = request.user
        blogs = Create.objects.filter(user=user).order_by('-date')
        return render(request, 'profile.html', {'user': user, 'blogs': blogs})
    else:
        messages.error(request, '⚠️ User must be Logged-in')
        return redirect('login')
    return render(request, 'profile.html', {'user': request.user})

def edit_blog(request, slug):
    blog = get_object_or_404(Create, slug=slug)
    if request.user != blog.user:
        messages.error(request, "⚠️ You don't have permission to edit this blog post.")
        return redirect('base')
    
    if request.method == "POST":
        blog.title = request.POST.get('btitle')
        blog.content = request.POST.get('bcontent')
        blog.save()
        messages.success(request, '✅ Blog updated successfully')
        return redirect('base')
    
    return render(request, 'edit.html', {'blog': blog})

def delete_blog(request, slug):
    blog = get_object_or_404(Create, slug=slug)
    if request.user != blog.user:
        messages.error(request, "⚠️ You don't have permission to delete this blog post.")
        return redirect('base')
    
    if request.method == "POST":
        blog.delete()
        messages.success(request, "✅ Blog post deleted successfully!")
        return redirect('base')
    return render(request, 'delete.html', {'blog': blog})