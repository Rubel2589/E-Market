from django.contrib import admin
from emarket_app.models import contact_form , brand_type_form , register_form , product_type ,product_category ,product_info , cart_details , order_address


# Register your models here.
admin.site.site_header = 'Emarket'
admin.site.site_title = 'Emarket'


class Contact_form_admin(admin.ModelAdmin):
    list_display = ['id','email']
    list_filter = ['contact','email']

class register_form_admin(admin.ModelAdmin):
    list_display = ['id','email']
    list_filter = ['first_name','email']


class brand_type_form_admin(admin.ModelAdmin):
    list_display = ['id','name','brand_location','brand_description']
    list_filter = ['name','brand_location']
    list_editable = ['name','brand_location','brand_description']

class product_type_admin(admin.ModelAdmin):
    list_display = ['id','name','product_image']
    list_filter = ['name']
    # list_editable = ['name','product_image']

class product_category_admin(admin.ModelAdmin):
    list_display = ['id','name']
    list_filter = ['name']
    # list_editable = ['name','product_image']

class product_info_admin(admin.ModelAdmin):
    list_display=['id','product_name','brand_name','product_type','price','discount','color']

class cart_details_admin(admin.ModelAdmin):
    list_display=['id','pro_name','user_email','pro_id','brand_name','product_type_name','product_category_name','price','discount','status','quantity','order_id','order_adres']

class order_address_admin(admin.ModelAdmin):
    list_display=['address_type','user_email','full_name','address','country','state']

admin.site.register(contact_form,Contact_form_admin)
admin.site.register(register_form,register_form_admin)
admin.site.register(brand_type_form,brand_type_form_admin)
admin.site.register(product_type,product_type_admin)
admin.site.register(product_category,product_category_admin)
admin.site.register(product_info,product_info_admin)
admin.site.register(cart_details,cart_details_admin)
admin.site.register(order_address,order_address_admin)


