from django import forms
from .models import product

class productFrom(forms.ModelForm):  
    class Meta:
        model = product
        fields = ("name","desc","price","available","stock")
        