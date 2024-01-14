from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class contact_form(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    brand_type = models.CharField(max_length=250)
    subject= models.CharField(max_length=250)
    contact=models.IntegerField()
    message=models.TextField()

    def __str__(self):
        return(self.email)


class brand_type_form(models.Model):
    name = models.CharField(max_length=200)
    brand_location = models.CharField(max_length=200)
    brand_description = models.TextField()
    brand_image = models.ImageField(upload_to = 'brand_image')
    def __str__(self):
        return str(self.name)


class register_form(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=200) 
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d',null=True)


class product_type(models.Model):
    name=models.CharField(max_length=100,null=True)
    product_image = models.ImageField(upload_to = 'product_type')
    def __str__(self):
        return str(self.name)

class product_category(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.name)


class product_info(models.Model):
    product_name = models.CharField(max_length=300)
    brand_name=models.ForeignKey(brand_type_form,on_delete=models.CASCADE)
    product_category=models.ForeignKey(product_category,on_delete=models.CASCADE)
    product_type=models.ForeignKey(product_type,null=True,on_delete=models.CASCADE)
    price=models.IntegerField()
    discount=models.IntegerField()
    description=models.TextField(max_length=500)
    product_img=models.ImageField(upload_to='product_image')
    color=models.CharField(max_length=100)
    def __str__(self):
        return str(self.product_name)


class order_address(models.Model):
    Choices=(
            ('Home','1'),
            ('Work','2')
        )
    address_type=models.CharField(max_length=50,choices=Choices)
    user_id=models.CharField(max_length=100)
    user_email=models.CharField(max_length=200)
    full_name=models.CharField(max_length=200)
    contact=models.CharField(max_length=300)
    address=models.CharField(max_length=200) 
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    pin_code=models.IntegerField()
    
    def __str__(self):
        return self.full_name
       


class cart_details(models.Model):
    user_id=models.IntegerField()
    user_email=models.CharField(max_length=200)
    brand_name=models.CharField(max_length=100)
    product_type_name=models.CharField(max_length=100)
    product_category_name=models.CharField(max_length=100)
    pro_id=models.CharField(max_length=200)
    pro_name=models.CharField(max_length=200,null=True)
    pro_image = models.CharField(max_length=400,null=True)
    price=models.IntegerField()
    discount=models.IntegerField(null=True)
    quantity=models.CharField(max_length=100,default=1)
    order_id=models.CharField(max_length=200,null=True,default='')
    order_adres=models.ForeignKey(order_address,on_delete=models.CASCADE,null=True,default='')
    status=models.CharField(max_length=100,default=0)
    

 