from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from djangoauth.models import CustomUser

# class VendorSerializer(serializers.ModelSerializer):
  
#   class Meta:
#     model=CustomUser
#     fields=['id','user','address']

#   def init_(self,*args,**kwargs):
#       super(VendorSerializer,self)._init_(*args,**kwargs)
#       self.Meta.depth=1

class ProductCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=ProductCategory
    fields='__all__'


class ProductCategoryDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model=ProductCategory
    fields='__all__'



# class VendorDetailSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=CustomUser
#     fields=['id','user','address']

#   def init_(self,*args,**kwargs):
#     super(VendorDetailSerializer,self)._init_(*args,**kwargs)
#     self.Meta.depth=1


class ProductListSerializer(serializers.ModelSerializer):
  product_ratings=serializers.StringRelatedField(many=True,read_only=True)
  #vendor=VendorSerializer()
  category=ProductCategorySerializer()
  class Meta:
    model=Product
    fields=['id','category','vendor','title','detail','price','product_ratings','slug','tag_list','image']

  def init_(self,*args,**kwargs):
    super(ProductListSerializer,self)._init_(*args,**kwargs)
    self.Meta.depth=1

class ProductImageSerializer(serializers.ModelSerializer):
  class Meta:
    model=ProductImage
    fields='__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
  product_ratings=serializers.StringRelatedField(many=True,read_only=True)
  product_imgs=ProductImageSerializer(many=True,read_only=True)
  #vendor=VendorSerializer()
  category=ProductCategorySerializer()
  class Meta:
    model=Product
    fields=['id','category','vendor','title','detail','price','slug','tag_list','product_ratings','product_imgs','demo_url']

  def init_(self,*args,**kwargs):
    super(ProductListSerializer,self)._init_(*args,**kwargs)
    self.Meta.depth=1


# class CustomerSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=CustomUser
#     fields='__all__' 

# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model=User
#     fields=['id','username','first_name','last_name','email']

# class CustomerDetailSerializer(serializers.ModelSerializer):
#   user=UserSerializer()
#   class Meta:
#     model=CustomUser
#     fields=['id','user','profile_img']


class OrderSerializer(serializers.ModelSerializer):
  
  class Meta:
    model=Order
    fields=['id','user','order_time','order_status']

class OrderItemsSerializer(serializers.ModelSerializer):
  order=OrderSerializer()
  product=ProductDetailSerializer()
  
  class Meta:
    model=OrderItems
    fields=['id','order','product','qty','price']

class OrderDetailSerializer(serializers.ModelSerializer):
  order=OrderSerializer()
  product=ProductListSerializer()
  
  class Meta:
    model=OrderItems
    fields='__all__'


# class CustomerAddressSerializer(serializers.ModelSerializer):
#   customer=CustomerSerializer()
  
  
#   class Meta:
#     model=CustomerAddress
#     fields='__all__'

class ProductRatingSerializer(serializers.ModelSerializer):
  #customer=CustomerSerializer()
  product=ProductListSerializer()
  
  class Meta:
    model=ProductRating
    fields='__all__'

# class RegistrationSerializer(serializers.ModelSerializer):
#   password2=serializers.CharField(write_only=True,style={'input_type':'password'})
#   class Meta:
#     model=User
#     fields=['id','username','first_name','last_name','email','password','password2']
#     extra_kwags={
#       'password':{'write_only':True}
#          }
    

#   def save(self):
    

#     password=self.validated_data['password']
#     password2=self.validated_data['password2']

#     if password!=password2:
#       raise serializers.ValidationError({'error':'p1 and p2 should be same'})
    
#     if User.objects.filter(email=self.validated_data['email']).exists():
#       raise serializers.ValidationError({"error":"email is already exists"})
    
#     account = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username'],
#             first_name=self.validated_data.get('first_name'),
#             last_name=self.validated_data.get('last_name')
#         )
    
#     # account=User(username=self.validated_data['username'],email=self.validated_data['email'])
#     account.set_password(password)
#     account.save()

#     return account
  
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user:
#                 if not user.is_active:
#                     raise serializers.ValidationError('User is deactivated.')
#             else:
#                 raise serializers.ValidationError('Unable to log in with provided credentials.')
#         else:
#             raise serializers.ValidationError('Must include "username" and "password".')

#         data['user'] = user
#         return data

#     def save(self, **kwargs):
#         user = self.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return {
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email,
#             'username':user.username,
#         }
    



    




