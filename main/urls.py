from django.urls import path
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router=routers.DefaultRouter()
#router.register('address',CustomerAddressViewSet)
router.register('productrating',ProductRatingViewSet)

urlpatterns = [
   
    # vendors
    #path('vendors/',VendorList.as_view()),
    #path('vendors/<int:pk>',VendorDetail.as_view()),
    #Products
    path('Products/',ProductList.as_view()),
    path('Products/<str:tag>',TagProductList.as_view()),
    path('Product/<int:pk>',ProductDetail.as_view()),
    path('Related-products/<int:pk>',RelatedProductList.as_view()),
    path('ProductCategory/',ProductListWithCategory.as_view()),
    path('AllProductCategory/<int:pk>',AllProductListWithCategory.as_view()),
    
    #Product Categories
    path('Categories/',CategoryList.as_view()),
    path('Category/<int:pk>',CategoryDetail.as_view()),
    #Customers
    #path('customers/',CustomerList.as_view()),
    #path('customer/<int:pk>',CustomerDetail.as_view()),
    #path('user/<int:pk>',UserDetail.as_view()),
    #path('customer/login',Login_view,name='customer_login'),
    #path('customer/register',registration_view,name='customer_register'),
    #Orders
    path('orders/',OrderList.as_view()),
    path('orderitems/',OrderItemsList.as_view()),
    path('customer/<int:pk>/orderitems/',CustomerOrderItemsList.as_view()),
    path('update-order-status/<int:order_id>',update_order_status),
    path('order/<int:pk>',OrderDetail.as_view()),
]

urlpatterns+=router.urls
