from typing import FrozenSet
from django.urls import path

from custom import views
from .views import *


urlpatterns = [
    path ('',views.index,name='index'),
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    
    
    path('product/',views.product_view, name='product'),
    path('customer/',views.customer_view, name='customer'),
    path('Customer_address/',views.customerAddress_view, name='customer_address'),
   
    path('category/',views.Category_view,name='category'),
    path('orders/',views.order_view,name='orders'),
    path('orderinfo/<int:id>',views.orderinfo,name='orderinfo'),
    path('banner/',views.Bannersview,name='banner'),
    path('createbanner/',views.createbanner,name='createbanner'),
    path('deletebanner/<int:id>/',views.delete_banner,name='deletebanner'),
    path('update_banner/<int:id>/',views.update_banner,name='update_banner'),
    
    
    
    path('attributes/',views.product_attr_view,name='attributes'),
    path('assc/',views.product_attr_assc_view,name='assc'),
    path('create_assoc/',views.create_attr_assoc,name='create_assoc'),
    path('update_assc/<int:id>',views.update_assoc,name='update_assc'),
    path('delete_assc/<int:id>',views.delete_assoc,name='delete_assc'),
    
    
    path('attribut_value/',views.product_attr_value_view,name='attribut_value'),
    path('updateattribute_value/<int:id>',views.update_attrvalue,name='updateattribute_value'),
    path("deleteattribute_value/<int:id>", views.delete_attrvalue, name="deleteattribute_value"),
    
    
    path('contactus/',views.Contactus,name='contactus'),
    path('custreport/',views.report,name='custreport'),
    
    path('create_attribute_value/',views.create_attr_value,name='create_attribute_value'),
    
    
    path('create_attribute/',views.create_attr,name='create_attribute'),
    path('update_attr/<int:id>/',views.update_attr,name='update_attr'),
    path('delete_attr/<int:id>/',views.delete_attr,name='delete_attr'),
    
    path('report/',views.report,name='report'),
    path('sales/',views.salesreport,name='sales'),
    
    
    
    
    
    
    path('coupons/',views.Coupon_view,name='coupons'),
    path('create_coupon/',views.Create_coupon,name='create_coupon'),
    path('delete_coupon/<int:id>/',views.delete_coupon,name='delete_coupon'),
    path('update_coupon/<int:id>/',views.update_coupon,name='update_coupon'),
    
    
    path('create_product/',views.create_Product,name='create_product'),
    #path('update_product/<int:id>/',views.update_product,name='update_product'),
    path('updateproduct/<int:pk>/',updateproduct.as_view(),name='updateproduct'),
    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
    
    path('create_category/',views.create_category,name='create_category'),
    path('delete_category/<int:id>/',views.delete_category,name='delete_category'),
    path('update_category/<int:id>/',views.update_category,name='update_category'),
    
    path('email/',views.Email,name='email'),
  
    
    path('productimage/',views.ProductImageview,name='productimage'),
    path('createproductimg/',views.CreateProductImage,name='createproductimg'),
    path('updateproductimg/<int:id>/',views.update_productimg,name='updateproductimg'),
    path('deleteproductimg/<int:id>/',views.delete_productimg,name='deleteproductimg'),
]

