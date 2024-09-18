from django import forms
from .models import OrenjiEntry

class OrenjiEntryForm(forms.ModelForm):
    class Meta:
        model = OrenjiEntry
        fields = ['product_name', 'price', 'descriptions', 'stock']
