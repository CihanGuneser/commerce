from django import forms
from django.forms.fields import ImageField
from django.forms.widgets import FileInput, NumberInput, TextInput, Textarea
from .models import Listing

class ListingForm(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = ('user_id','item_name','product_category','product_details','listing_image_link','listing_image','price')

    
    #user_id = models.ForeignKey(User, on_delete=CASCADE)  #many to one relationship with User model
    #listing_image = models.ImageField(blank = True, upload_to='static/img/%Y/%m/%d')