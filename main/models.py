from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# After changes have been made to models, run python manage.py makemigrations (similar to adding changes to staging area),
# then python manage.py migrate (to make changes)

class MedicalHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # step 1 fields
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=50)
    # step 2 fields
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    # step 3 Fields
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    # state
    zipcode = models.CharField(max_length=50)

    # step 4 fields
    # taking_meds = models.CharField(max_length=3, choices=TAKING_MEDS_CHOICES)
    # step 5 fields
    # all_is_accurate = models.BooleanField(default=False)

    def __str__(self):
        return f"MedicalHistory object for {self.fname} {self.lname}"

