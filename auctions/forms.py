from django import forms
from django.forms.widgets import TextInput, Textarea

class ListingForm(forms.Form):
    product_category = forms.CharField(widget=TextInput(attrs={'autocomplete':'off'}))
    product_details = forms.CharField(widget=Textarea)
    item_name = forms.CharField()
    listing_image = forms.ImageField()
    listing_image_link = forms.CharField()
    most_recent_bid = forms.DecimalField()