from django.shortcuts import render ,  redirect
from django.http import HttpResponse
from .models import Event
from django.forms import ModelForm
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated :
        return HttpResponseRedirect(reverse("login"))
    return render(request, "event_list.html")
    
def login_view(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username , password=password )
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "user/login.html", {"message" : "Invalid info "})
    return render(request, "user/login.html")

def logout_view(request):
    logout(request)
    return render(request, "user/login.html", {"message" : "Logged out "})

def account(request): 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username,password=password)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "user/account.html" )

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_event.html', {'form': form ,"message" : "Added successfully"})
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def event_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_delete.html', {'event': event})

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location']

def event_update(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_detail', event_id=event.id)
    return render(request, 'event_update.html', {'form': form, 'event': event})