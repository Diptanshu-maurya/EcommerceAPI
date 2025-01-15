from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from djangoauth.models import CustomUser

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


# Create your models here.

# class Vendor(models.Model):
#   user=models.ForeignKey(User,on_delete=models.CASCADE)
#   address=models.TextField(null=True)

#   def __str__(self):
#     return self.user.username


class ProductCategory(models.Model):
  title=models.CharField(max_length=100)
  detail=models.TextField(null=True)

  def __str__(self):
    return self.title
  

class Product(models.Model):
  category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name='category_product')
  user=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)
  # vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
  title=models.CharField(max_length=100)
  detail=models.TextField(null=True)
  price=models.FloatField()
  slug=models.CharField(max_length=200,unique=True,null=True)
  tags=models.TextField(null=True)
  image=models.ImageField(upload_to='product_imgs',null=True)
  demo_url=models.URLField(null=True,blank=True)

  def __str__(self):
    return self.title
  
  def tag_list(self):
    tagList=self.tags.split(',')
    return tagList
  


# class Customer(models.Model):
#   user=models.ForeignKey(User,on_delete=models.CASCADE)
#  # mobile=models.PositiveBigIntegerField(unique=True)
#   profile_img=models.ImageField(upload_to='customer_imgs',blank=True,null=True)

#   def __str__(self):
#     return self.user.username

class Order(models.Model):
 # customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_orders') 
  user=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, blank=True)
  order_time=models.DateTimeField(auto_now_add=True)
  order_status=models.BooleanField(default=False)
  
  # def __str__(self):
  #    return self


class OrderItems(models.Model):
  order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')
  product=models.ForeignKey(Product,on_delete=models.CASCADE) 
  qty=models.IntegerField(default=1)
  price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
   
  def __str__(self):
    return self.product.title
  
class CustomerAddress(models.Model):
  user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='order_addreses', null=True, blank=True)
  address=models.TextField()
  default_address=models.BooleanField(default=False) 
   
  def __str__(self):
    return self.address
  

class ProductRating(models.Model):
  user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='rating_customers', null=True, blank=True)
  rating=models.IntegerField()
  reviews=models.TextField()
  add_time=models.DateTimeField(auto_now_add=True)
  product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_ratings')

  def __str__(self):
    return f'{self.rating}-{self.reviews}'
  

class ProductImage(models.Model):
  product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_imgs')
  image=models.ImageField(upload_to='product_imgs/',null=True)

  def __str__(self):
    return self.image.url
  
