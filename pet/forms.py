from django import forms
from .models import Pet


class PetSaleForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'vaccunes', 'category', 'breed', 'image','description','discount','price']
