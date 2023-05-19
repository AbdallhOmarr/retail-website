"""retail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("products/", views.products, name="products"),
    path("cart/", views.cart, name="cart"),
    path("payment/", views.payment, name="payment"),
    path('products/<slug:slug>/',views.product_detail, name = 'product_detail'),
    path("about/", views.about, name="about"),
    path("client/", views.client, name="client"),
    path("contact/", views.contact, name="contact"),

    path('login_register/', views.login_or_register, name='login_register'),
    path("checkout/", views.checkout, name="checkout"),
    path('logout/', views.logout_function, name='logout'),
    path('vueapp/',views.vueapp,name='vueapp'),

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    # path('profile/<slug:slug>',views.profile,name='profile'),
]