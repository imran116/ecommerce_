from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('women/', views.get_women_product, name='women'),
    path('men/', views.get_men_product, name='men'),
    path('accessories/', views.get_accessories_product, name='accessories'),
    path('kid/', views.get_kid_product, name='kid'),
    path('all-products/', views.get_all_products, name='all_products'),
    path('subscribe/', views.SubscriberView.as_view(), name='subscriber'),
    path('aboutus/', views.get_aboutus_section, name='about-us'),
    path('single-product/<int:product_id>/', views.ProductsDetails.as_view(), name='single-product'),
    path('buy-product/<int:product_id>/', views.BuyProducts.as_view(), name='buy-product'),
    path('add-to-card/<int:product_id>/', views.add_to_cart, name='add-to-card'),
    path('card-view/', views.cart_view, name='cart_view'),
    path('delete-card/<int:cart_id>/', views.remove_from_cart, name='delete-cart'),


]
