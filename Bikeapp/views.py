from django.shortcuts import render
from .models import Car





# Create your views here.

def home(request):
    Vaccine=Car.objects.all()
    return render(request,'home.html',{"Vaccine":Vaccine})

