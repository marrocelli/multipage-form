from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import MedicalHistory

# Create your views here.

def index(response):
    context = {}
    return render(response, "main/base.html", context)

def home(response):
    """
    Handles all webiste interactions on home page.
    """
    context = {}
    return render(response, "main/home.html", context)

def account(response):
    """
    Handles all webiste interactions on user account page.
    """
    
    # If user has a medical history in database
    if MedicalHistory.objects.filter(user=response.user):
        medical_history = response.user.medicalhistory

        # Use Django's to-python queryset serializer to serialize data to send to template.
        data = serializers.serialize("python", MedicalHistory.objects.filter(user=response.user))
    else: # 
        data = None
    context = {"data": data}
    return render(response, "main/account.html", context)

def form(response):
    """
    Handles all webiste interactions on form page. Currently only deals with
    Medical History form and saves form data to database.
    """
    if response.method == "POST":
        
        # Create MedicalHistory object with form data.
        user = response.user
        fname = response.POST.get("fname")
        lname = response.POST.get("lname")
        email = response.POST.get("email")
        phone = response.POST.get("phone")
        age = response.POST.get("age")
        gender = response.POST.get("gender")
        address1 = response.POST.get("address1")
        address2 = response.POST.get("address2")
        city = response.POST.get("city")
        zipcode = response.POST.get("zipcode")
        new_medical_history = MedicalHistory(
            user=user, fname=fname, lname=lname, email=email, 
            phone=phone, age=age, gender=gender,
            address1=address1, address2=address2,
            city=city, zipcode=zipcode
        )
        new_medical_history.save()
        
        # Redirect to account page after form submitted.
        return redirect("/account")

    context = {}
    return render(response, "main/form.html", context)
