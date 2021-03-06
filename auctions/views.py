from datetime import date
from typing import List, NoReturn
from django.contrib.auth import authenticate, login, logout, models
from django.contrib.auth.models import User
from django.core import exceptions 
from django.db import IntegrityError
from django.db.models.fields import AutoField
from django.http import HttpResponse, HttpResponseRedirect
from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from .models import Bid, Category, Comment, Listing, User
from .forms import ListingForm

def watchlist_view(request, item_id):
    item = get_object_or_404(Listing, pk=item_id)
    watchlisted=False
    if item.watchlist.filter(id=request.user.id).exists():
        item.watchlist.remove(request.user)
        watchlisted=False
    else:
        item.watchlist.add(request.user)
        watchlisted=True
    
    return HttpResponseRedirect(reverse('item', args=[item_id]))

def index(request): 
    return render(request, "auctions/index.html", {
        'Listing':Listing.objects.all(),
        'Category':Category.objects.all()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    form = ListingForm(initial={'user':request.user})
    return render(request,"auctions/create_listing.html", {
        'form':form}
    )

def save(request):
    if request.method =='POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse("index"))

def item_view(request,item_id):

    item = get_object_or_404(Listing, pk=item_id)

    if item.watchlist.filter(id=request.user.id).exists():
        button_tag="Remove_from_watchlist"
    else:
        button_tag="Add_to_watchlist"

    try:
        comments = Comment.objects.filter(listing=item_id).order_by('-date')
    
    except ObjectDoesNotExist:
        comments = None

    try: 
        bid = Bid.objects.filter(listing=item_id).latest('date')
        min_bid = float(bid.bid) + 0.01
         
    except ObjectDoesNotExist:
        bid = None
        min_bid = float(item.price) + 0.01
    
    if min_bid < item.price:
        min_bid = float(item.price) + 0.01
            
    #item = Listing.objects.get(pk=item_id)
    return render(request,"auctions/item.html",{
        "name":item.item_name,
        "item_id":item.id,
        'price':item.price,
        'details':item.product_details,
        'listing_image': item.listing_image.url,
        'button_tag':button_tag,
        'bid':bid,
        'min_bid':min_bid,
        'item_user':item.user,
        'bid_closed':bid.closed,
        'comments':comments
    })
  
def user_watchlist_view(request,user_id):
   
    watchlist_items = Listing.objects.filter(watchlist__id=user_id)

    return render(request,"auctions/user_watchlist.html",{
        #'name':User.objects.get(pk=user_id),
        #'watchlist_items':Listing.objects.get(pk=user_id)
        'watchlist_items':watchlist_items
    })

def place_bid_view(request,item_id):
    if request.method =='POST':
        newest_bid = request.POST["newest_bid"]
        bid_user= request.user
        bid_listing = Listing(pk=item_id)
        b=Bid(bid=newest_bid, user = bid_user, listing = bid_listing)
        b.save()
    
    return HttpResponseRedirect(reverse("item", args= {item_id}))

def close_bid_view(request, item_id):
    if request.method=='POST':
        latest_bid = Bid.objects.filter(listing=item_id).latest('date')
        latest_bid.closed = True
        latest_bid.save()

        item = get_object_or_404(Listing, pk=item_id)
        item.last_accepted_bid = latest_bid.bid
        item.save()

    return HttpResponseRedirect(reverse("item", args= {item_id,}))

def save_comment_view(request,item_id):

    if request.method=='POST':
        c = Comment(title = request.POST['comment_title'], 
                    text = request.POST['comment_details'],
                    date = timezone.datetime.now,
                    user = request.user,
                    listing = Listing.objects.get(pk=item_id))
        c.save()
    return HttpResponseRedirect(reverse("item", args={item_id,}))

def categorize_view(request):
    
    if request.method=='POST':
        selected_category_id=Category.objects.get(pk=request.POST['select_category']).id

    if selected_category_id==16: #means 'All' selected. id of All is 16. 
        Listed_items = Listing.objects.all()
    else:
        Listed_items = Listing.objects.filter(product_category=selected_category_id)

    return render(request, "auctions/index.html", {
        'Category': Category.objects.all(),
        'Listing': Listed_items,
        'number_of_listing_in_the_cat': Listed_items.count(),
        'selected_category_name': Category.objects.get(pk=selected_category_id).name
    })

def dummy(request):
    return render(request, "auctions/dummy.html")