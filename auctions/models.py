from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    pass

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)  #many to one relationship with User model
    item_name = models.CharField(max_length=64, blank=False)
    product_category = models.CharField(max_length=32, blank=False)
    product_details = models.TextField(max_length=256, blank=False)
    listing_image_link = models.CharField(max_length=256,blank=True )
    listing_image = models.ImageField(blank = True, upload_to='img/%Y/%m/%d')
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    watchlist = models.ManyToManyField(User,related_name='watchlist',default=None, blank=True)
    last_accepted_bid = models.DecimalField(decimal_places=2, max_digits=6, default=0 )

    def __str__(self):
        return f"Listing id: {self.pk}, item: {self.item_name} "

class Bid(models.Model):

    bid = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    user = models.ForeignKey(User, on_delete=CASCADE)
    listing = models.ForeignKey(Listing, on_delete=CASCADE)
    date  = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"Bid id: {self.pk}, {self.listing_id}, created at {self.date} "

class Comment(models.Model):
    title = models.CharField(max_length=32, blank=False)
    text = models.TextField(max_length=256,blank=False)
    date = models.DateTimeField(auto_now_add=True) ##You can adjust this one 
    user = models.ForeignKey(User, on_delete=CASCADE)
    listing = models.ForeignKey(Listing, on_delete=CASCADE)

    def __str__(self):
        return f"Comment id: {self.id}, on item: {self.listing}, created at {self.date}"