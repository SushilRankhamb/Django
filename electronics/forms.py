from django import forms
from .models import Car

class ProductForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'color', 'price', 'available', 'stock', 'image']
