from django import forms
from djangoform.models import Contact

# form class inheriting from ModelForm that takes in the model and fields
# inputs: first name, last name, email
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email']
