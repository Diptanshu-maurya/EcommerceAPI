from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions, viewsets
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from djangoauth.models import CustomUser


# Create your views here.

# class VendorList(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = VendorSerializer


# class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = VendorDetailSerializer


class ProductList(generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    def get_queryset(self):
        qs=super().get_queryset()
        if 'category' in self.request.GET:
            category=self.request.GET['category']
            category=ProductCategory.objects.get(id=category)
        if 'fetch_limit' in self.request.GET:
            limit=int(self.request.GET['fetch_limit'])
            qs=qs[:limit]
        return qs



class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# class CustomerList(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomerSerializer


# class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomerDetailSerializer
#     pagination_class=None

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     pagination_class=None

# @csrf_exempt
# def customer_login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(username=username, password=password)
#     if user:
#         customer=Customer.objects.get(user=user)
#         msg = {
#             'bool': True,
#             'user': user.username,
#             'id':customer.id,
#         }
#     else:
#         msg = {
#             'bool': False,
#             'msg': 'Invalid username or password'
#         }
#     return JsonResponse(msg)

# @csrf_exempt
# def customer_register(request):
#     first_name = request.POST.get('firstname')
#     last_name = request.POST.get('lastname')
#     username = request.POST.get('username')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     mobile = request.POST.get('mobile')
#     try:
#         user = User.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#             password=password,
#         )
#         if user:
#             try:
#                 customer = Customer.objects.create(
#                     user=user,
#                     mobile=mobile
#                 )
#                 msg = {
#                     'bool': True,
#                     'user': user.id,
#                     'customer': customer.id,
#                     'msg': 'Thank you for registration'
#                 }
#             except IntegrityError:
#                 msg = {
#                     'bool': False,
#                     'msg': 'mobile already exist!!!'
#                 }
#         else:
#             msg = {
#                 'bool': False,
#                 'msg': 'Something went wrong!!!'
#             }
#     except IntegrityError:
#         msg = {
#             'bool': False,
#             'msg': 'username already exist!!!'
#         }
#     return JsonResponse(msg)

def customer_login(request):
    pass


def customer_register(request):
    pass



class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def get_queryset(self):
    #     userId=self.kwargs['userId']
    #     user=User.objects.get(pk=userId)
    #     order=Order.objects.filter(user=user)
    #     return order
class OrderItemsList(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

class CustomerOrderItemsList(generics.ListAPIView):
     queryset = OrderItems.objects.all()
     serializer_class = OrderItemsSerializer
     pagination_class = None

     def get_queryset(self):
         qs=super().get_queryset()
         user_id=self.kwargs['pk']
         
         
         q=OrderItems.objects.filter(order__user__id=user_id)
         return q
        # user_id=self.kwargs['pk']
        # order=Order.objects.get(user_id=user_id)
        # order_id=order.id
        # orders=OrderItems.objects.filter(order_id=order_id)
        # return orders


    

class OrderDetail(generics.ListAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        order_item = OrderItems.objects.filter(order=order)
        return order_item

# class CustomerAddressViewSet(viewsets.ModelViewSet):
#     serializer_class = CustomerAddressSerializer
#     queryset = CustomerAddress.objects.all()

class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ProductRatingSerializer
    queryset = ProductRating.objects.all()

class CategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class=None

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategoryDetailSerializer

class ProductListWithCategory(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET['category']
        qs = qs.filter(category=category)
        return qs
class AllProductListWithCategory(APIView):
    def get(self,request,pk):
        product=Product.objects.filter(category=pk)
        serializer=ProductListSerializer(product,many=True)
        
        return Response(serializer.data)


    

class TagProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        
        tag = self.kwargs['tag']
        #tag = self.request.GET['tag']
        qs = qs.filter(tags__icontains=tag)
        #qs=Product.objects.filter(tags__icontains=tag)
        return qs

class RelatedProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        product_id = self.kwargs['pk']
        product = Product.objects.get(id=product_id)
        qs = qs.filter(category=product.category).exclude(id=product_id)
        return qs
    
# @api_view(['POST'])
# def registration_view(request):
#     print(request)
#     if request.method =='POST':
#         serializer=RegistrationSerializer(data=request.data)
#         print("data:",request.data)

#         data={}
#         if serializer.is_valid():
#             account=serializer.save()
#             data['response']=True
#             data['msg']='registration successful'
#             data['username']=account.username
#             data['firstname']=account.first_name
#             data['lastname']=account.last_name
#             data['email']=account.email
#             data['id']=account.id
#             token, created = Token.objects.get_or_create(user=account)
#             data['token'] = token.key

            

#             # token=Token.objects.get(user=account).key
#             # data['token']=token

#         else:
#             data['response']=False
#             data['error']=serializer.errors
#         return Response(data)
    
# @api_view(['POST'])
# def Login_view(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     data = serializer.save()
#     return Response(data)

@csrf_exempt
def update_order_status(request,order_id):
    if request.method=='POST':
        updateRes=Order.objects.filter(id=order_id).update(order_status=True)
        msg={
            'bool':False
        }
        if updateRes:
            msg={
                'bool':True
            }
    return JsonResponse(msg)




    

