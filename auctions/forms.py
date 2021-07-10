from django import forms
from django.forms.fields import ImageField
from django.forms.widgets import FileInput, NumberInput, TextInput, Textarea
from .models import Listing

class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = ('product_category','product_details','item_name','listing_image_link','most_recent_bid')

    
    #user_id = models.ForeignKey(User, on_delete=CASCADE)  #many to one relationship with User model
    #listing_image = models.ImageField(blank = True, upload_to='static/img/%Y/%m/%d')