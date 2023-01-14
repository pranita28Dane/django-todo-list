from django import forms
from django.forms import models
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]