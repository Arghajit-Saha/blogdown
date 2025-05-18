from django.shortcuts import render, redirect, get_object_or_404
from .models import Create, Contact
# Create your views here.

def base(request):
    blogs = Create.objects.all().order_by('-date')
    return render(request, 'content.html', {'blogs' : blogs})

def create(request):
    if request.method == "POST":
        create = Create()
        create.title = request.POST.get('btitle')
        create.content = request.POST.get('bcontent')
        create.save()
        return redirect('base')
    return render(request, 'create.html')

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