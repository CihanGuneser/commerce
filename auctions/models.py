from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    pass

class Listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=CASCADE)  #many to one relationship with User model
    item_name = models.CharField(max_length=64, blank=False)
    product_category = models.CharField(max_length=32, blank=False)
    product_details = models.TextField(max_length=256, blank=False)
    listing_image_link = models.CharField(max_length=256,blank=True )
    listing_image = models.ImageField(blank = True, upload_to='static/img/%Y/%m/%d')
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=False)

    def __str__(self):
        return f"Listing id: {self.pk}, item: {self.item_name} "

class Bid(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    Listing_id = models.ForeignKey(Listing, on_delete=CASCADE)

    def __str__(self):
        return f"Bid id: {self.pk}, {self.Listing_id} "

class Comment(models.Model):
    comment_title = models.CharField(max_length=32, blank=False)
    comment_text = models.TextField(max_length=256,blank=False)
    comment_time = models.DateTimeField(auto_now_add=True) ##You can adjust this one 
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=CASCADE)

    def __str__(self):
        return f"Comment id: {self.id}, on item: {self.listing_id}, at {self.comment_time}"