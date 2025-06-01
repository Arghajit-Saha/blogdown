from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from blog.models import Create, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Count


# Create your views here.
def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')
    else:
        try:
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
            user_count = User.objects.count()
            blog_count = Create.objects.count()
            form_count = Contact.objects.count()
            return render(request, 'dashboard.html', {'user_count': user_count, 'blog_count': blog_count, 'form_count': form_count})
        else:
            messages.info(request, 'You are not authorized to access this page')
            return redirect('adminlogin')
    else:
        messages.info(request, 'You are not logged in')
        return redirect('adminlogin')
    
def users(request):
    users = User.objects.annotate(blog_count=Count('create'))
    return render(request, 'user.html', {'users': users})

def user_delete(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        user.delete()
        return redirect('users')
    return render(request, 'delete-user.html', {'user': user})

def blogs_admin(request):
    users = User.objects.all()
    for user in users:
        user.blogs = user.create_set.all()
    return render(request, 'blogs.html', {'users': users})

def blog_delete(request, slug):
    blog = get_object_or_404(Create, slug=slug)
    if request.method == "POST":
        blog.delete()
        return redirect('blogs')
    return render(request, 'delete-blog.html', {'blog': blog})

def contact(request):
    contacts = Contact.objects.all().order_by('-id')
    return render(request, 'contact-admin.html', {'contacts': contacts})

def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect('contact-admin')
    return render(request, 'delete-contact.html', {'contact': contact})