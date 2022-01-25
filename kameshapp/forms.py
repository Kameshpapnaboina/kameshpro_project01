from django import forms
from .models import kameshmodel

class kameshform(forms.ModelForm) :
     class Meta :
         model=kameshmodel
         fields= "__all__"