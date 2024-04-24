from django.shortcuts import render , redirect , reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.http import HttpResponse


@login_required
def home(request):
    return render(request,"home.html",{})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def information(request):
    if request.method == "POST":
       

        events_title = request.POST.get('events_title')
        events_description = request.POST.get('events_description')
        events_date = request.POST.get('events_date')
        events_time = request.POST.get('events_time')
        events_organizer_details = request.POST.get('events_organizer_details')
        events_location = request.POST.get('events_location')

        Events.objects.create(
            events_title =events_title,
            events_description = events_description,
            events_date = events_date,
            events_time = events_time,
            events_organizer_details = events_organizer_details,
            events_location = events_location,
        )
        
        return redirect('home:information')
    

    queryset = Events.objects.all()
    context = {'informations': queryset}
    return render(request, 'home.html',context)


def delete_information(request, id):
   queryset = Events.objects.get(id = id)
   queryset.delete()
   return redirect('home:information')


def update_information(request,id):
    queryset = Events.objects.get(id = id)
    if request.method == "POST":
        events_title = request.POST.get('events_title')
        events_description = request.POST.get('events_description')
        events_date = request.POST.get('events_date')
        events_time = request.POST.get('events_time')
        events_organizer_details = request.POST.get('events_organizer_details')
        events_location = request.POST.get('events_location')

        queryset.events_description = events_description
        queryset.events_title =events_title
        queryset.events_date = events_date
        queryset.events_time = events_time
        queryset.events_organizer_details = events_organizer_details
        queryset.events_location = events_location
        queryset.save()
        return redirect('home:information')
    
    context = {'informations': queryset}
    return render(request, 'update_information.html',context)
    
    
    
    



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    

