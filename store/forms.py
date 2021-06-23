from django import forms
from django.forms import ModelForm
from .models import Reviews,Contact

class formContact(forms.ModelForm):
  class Meta:
      model= Contact
      fields= ["name", "email", "message"]

class formReviews(forms.ModelForm):
    class Meta:
        model= Reviews
        fields= ["description",'ratings']
