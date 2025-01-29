"""
URL configuration for furnitureProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from website import views

urlpatterns = [
    path('',views.home),
    path('shop/',views.shop),
    path('product_details/',views.product_details),
    path('signup/',views.signup),
    path('create_account/',views.create_account),
    path('login/',views.login),
    path('login_process/',views.login_process),
    path('add_to_cart/',views.add_to_cart),
    path('cart/',views.cart),
    path('increaese_cart_qty/',views.increaese_cart_qty),
    path('checkout/',views.checkout),
    path('place_order/',views.place_order),
    path('Qr_code/',views. Qr_code),
    path('about/',views.about),
    path('services/',views.services),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('delete_product/',views.delete_product),
    path('save_contact/',views.save_contact),
    # path('Pyment/',views.Pyment),
    # path("verify_payment/",views.verify_payment),


    path('admin/', admin.site.urls),
   
]
