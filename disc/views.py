from django.shortcuts import render,redirect
from .models import Movies,Contact
from .forms import BookingForm


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    dict_contact={
        'contactkey':Contact.objects.all()
    }
    return render(request,'contact.html',dict_contact)
def order(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'order.html',dict_form)
def movies(request):
    dict_eve={
        'eve':Movies.objects.all()
    }
    return render(request,'movies.html',dict_eve)
    

