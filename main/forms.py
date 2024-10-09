from django import forms
from .models import OrenjiEntry
from django.utils.html import strip_tags

class OrenjiEntryForm(forms.ModelForm):
    class Meta:
        model = OrenjiEntry
        fields = ['product_name', 'price', 'descriptions', 'stock']

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)  # Menghapus tag HTML

    def clean_descriptions(self):
        descriptions = self.cleaned_data["descriptions"]
        return strip_tags(descriptions)  # Menghapus tag HTML
