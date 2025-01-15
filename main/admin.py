from django.contrib import admin
from .models import *
from djangoauth.models import CustomUser


# Register your models here.
# admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(ProductCategory)
# admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItems)
# admin.site.register(CustomerAddress)
admin.site.register(ProductRating)
admin.site.register(ProductImage)


