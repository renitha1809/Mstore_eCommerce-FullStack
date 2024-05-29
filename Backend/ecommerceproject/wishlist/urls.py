from django.urls import path
from .views import (
    WishlistAddView,
    WishlistListView,
    WishlistRemoveView
)

urlpatterns=[
    path('products/<str:id>/add_to_wishlist',WishlistAddView.as_view(),name='add-to-wishlist'),
    path('wishlist',WishlistListView.as_view(),name='wishlist'),
    path('wishlist/<int:id>',WishlistRemoveView.as_view(),name='wishlist-item-remove'),
]