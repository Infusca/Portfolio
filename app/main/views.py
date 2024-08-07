from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Tag
from .forms import ContactForm

# Create your views here.

def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
        
    return render(request, "contact.html", {'form': form})
    # return render(request, "contact.html")

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {'project': project})

def success(request):
    return render(request, "success.html")