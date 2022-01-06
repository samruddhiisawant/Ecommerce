from re import S
from django import forms
from django.db import models
from django.forms import fields, widgets
from customer.models import *
from orders.models import *
from store.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class CustomerAddressform(forms.ModelForm):
    class  Meta:
        model = Customer_Address
        fields ="__all__"


class ProductForm(forms.ModelForm):
    #special_price_from = forms.DateField(required=True, input_formats=["%Y-%m-%d", ])
    class Meta:
        model = Product
        fields = "__all__"
        
class Product_AttributeForm(forms.ModelForm):
    #special_price_from = forms.DateField(required=True, input_formats=["%Y-%m-%d", ])
    class Meta:
        model = Product_Attribute
        fields = "__all__"
        # exclude=['image','long_description','short_description','quantity','meta_description','meta_keyword','special_price_to','special_price_from','cat','created_by','modify_by','is_feature','status']
        #exclude=['created_by','modify_by']
        
        
class Product_Attribute_value_Form(forms.ModelForm):
    #special_price_from = forms.DateField(required=True, input_formats=["%Y-%m-%d", ])
    class Meta:
        model = Product_Attribute_values
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class  Meta:
        model = Category
        fields ="__all__"
        exclude=[]


class Emailform(forms.ModelForm):
    class  Meta:
        model = EmailTemplate
        fields ="__all__"
        exclude=[]
        

class Couponform(forms.ModelForm):
    class  Meta:
        model = Coupons
        fields ="__all__"
        exclude=[]

class ProductAttributeAssocform(forms.ModelForm):
    class Meta:
        model = Product_attribute_association
        fields="__all__"   
        
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields="__all__"
        # widgets={
        #     'product':
        # }
        
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategories
        fields="__all__"
        
class Bannerform(forms.ModelForm):
    class Meta:
        model = Banner
        fields="__all__"
        
    