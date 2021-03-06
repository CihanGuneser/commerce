from auctions import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("save", views.save, name="save"),
    path("item/<int:item_id>",views.item_view, name="item"),
    path("watchlist/<int:item_id>",views.watchlist_view, name='watchlist'),
    path("user_watchlist/<int:user_id>",views.user_watchlist_view, name='user_watchlist'),
    path("bid/<int:item_id>",views.place_bid_view,name='place_bid_view'),
    path("close_bid/<int:item_id>",views.close_bid_view, name='close_bid_view'),
    path('save_comment/<int:item_id>',views.save_comment_view, name='save_comment'),
    path("category",views.categorize_view, name='categorize_view'),
    path("dummy",views.dummy,name="dummy")
] 
