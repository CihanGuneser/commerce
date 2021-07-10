from typing import List
from django.contrib.auth import authenticate, login, logout, models
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Listing, User
from .forms import ListingForm

def index(request):
    return render(request, "auctions/index.html", {
        'Listing':Listing.objects.all(),
        #'Listing.listing_image.url':Listing.listing_image.name,
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
    form = ListingForm()
    return render(request,"auctions/create_listing.html", {
        'form':form}
    )

def save(request):
    if request.method =='POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            product_category = form.cleaned_data['product_category']
            product_details = form.cleaned_data['product_details']
            item_name = form.cleaned_data['item_name']
            #listing_image = form.cleaned_data['listing_image']
            listing_image_link = form.cleaned_data['listing_image_link']
            most_recent_bid = form.cleaned_data['most_recent_bid']

            print (form.cleaned_data)

    return HttpResponseRedirect(reverse("index"))

