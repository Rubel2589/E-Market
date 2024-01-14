"""emarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from emarket_app import views
from django.conf import settings   
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
# WEBSITE Page URL
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('navbar_page',views.navbar_page,name='navbar_page'),
    path('contact_page',views.contact,name='contact_page'),
    path('register_page',views.register_page,name='register_page'),
    path('login_page',views.login_page,name='login_page'),
    path('logout',views.logout_link,name='logout'),
    path('pro_type',views.pro_type,name='pro_type'),
    path('single_product_detail',views.single_product_detail,name='single_product_detail'),
    path('shop',views.shop_page,name='shop'),
    path('product_cate',views.product_cate,name='product_cate'),
    # ajax routes
        path('login_user_cart_data',views.login_user_cart_data,name='login_user_cart_data'),
        path('add_pro_cart',views.add_pro_cart,name='add_pro_cart'),
        path('show_cart_data',views.show_cart_data,name='show_cart_data'),
        path('add_order_address',views.add_order_address,name='add_order_address'),
        path('check_password',views.check_password_url,name='check_password'),
        path('check_email',views.check_email,name='check_email'),
        path('search_item_url',views.search_item_url,name='search_item_url'),

    # end
    path('checkout',views.checkout,name='checkout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('delete_product_url',views.delete_product_url,name='delete_product_url'),
    path('profile_image_change',views.profile_image_change,name='profile_image_change'),

    # paytm url 
    path('handlerequest',views.handlerequest,name='handlerequest'),
     

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
