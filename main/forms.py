from django import forms
from .models import MedicalHistory

# class MedicalHistoryForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=50)
#     check = forms.BooleanField()

# class PersonalDetailsForm(forms.ModelForm):
#     title = "Personal Details"
    
#     class Meta:
#         model = Person
#         fields = ('fname', 'lname', 'age', 'email', 'phone', 'gender')
#         labels = {
#             'fname': "First Name",
#             "lname": "Last Name"
#         }

#         help_texts = {}
#         error_messages = {}

class MedicalHistoryForm(forms.ModelForm):
    title = "Medical History"

    class Meta:
        model = MedicalHistory
        fields = ('taking_meds',)
