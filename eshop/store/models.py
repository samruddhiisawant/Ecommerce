from re import M, T
from typing import Match, Reversible
from django.conf.urls import url
from django.db.models.deletion import CASCADE
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.enums import Choices 
from django.conf import settings
# from django_better_choices import Choices
from django.urls import reverse
from django.db.models import *
from django.core.validators import MinValueValidator, MaxValueValidator

class CommonInfo(models.Model):
    #created_by  = models.IntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_created_by_user',on_delete=CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modify_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='%(class)s_modify_by_user',on_delete=CASCADE)
    #modify_by = models.IntegerField()
    modify_date = models.DateField(auto_now_add=True)
    class Meta:
        abstract = True


class Status(models.IntegerChoices):
    AVAILABLE=1
    NOT_AVAILABLE=0

class Category(CommonInfo):
    parent=models.ForeignKey("self" ,on_delete=models.SET_NULL,null=True,blank=True,related_name='child')
    name=models.CharField(max_length=100)
    status=models.IntegerField(choices=Status.choices)
    class Meta:
        unique_together=['parent']
     
    def __str__(self):
        if self.parent:
           return self.parent.name + ' - ' + self.name
        else:
          return self.name

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        verbose_name_plural = "Categories"


    


class Product(CommonInfo):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=CASCADE,blank=True,related_name='%(class)s_item_id')
    sku= models.CharField(max_length=45)
    short_description = models.CharField(max_length=100)
    long_description = RichTextField(blank= True , null = True)
    price = models.FloatField()
    special_price = models.FloatField()
    special_price_from = models.DateField(auto_now_add=False)
    status=models.BooleanField()
    quantity = models.IntegerField()
    meta_description = models.TextField()
    meta_keyword = models.TextField()
    status = models.BooleanField()
    is_feature = models.BooleanField()
    #image = models.ImageField(null=True, blank=True)
    created_date =models.DateField(auto_now=True)
    #created_by=models.IntegerField(default=True)
    #modify_by=models.IntegerField(default=True)
    #modify_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.name
    


    @property
    def checkOffer(self):
        if self.special_price_from > self.special_price_to:
            return self.price
        else :
            return self.special_price
    @property
    def is_available(self):
        return self.quantity > 0
    
    

class ProductImages(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, null=True)
    status =models.IntegerField(choices=Status.choices)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url
        
    
class SubCategories(models.Model):
    id=models.AutoField(primary_key=True)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    Product_id =models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("sub_category_list")

class Product_Attribute(CommonInfo):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=45)
    product=models.ForeignKey(Product,on_delete=CASCADE,blank=True,)
    
    def __str__(self):
        return self.name
        
    
    
class Product_Attribute_values(CommonInfo):
    id =models.AutoField(primary_key=True)
    product_attribute_id= models.ForeignKey(Product_Attribute,on_delete=CASCADE,blank=True,)
    product_Attribute_value =models.CharField(max_length=45)
    
    def __str__(self):
        return self.product_Attribute_value
    
class Product_attribute_association(models.Model):
    id=models.AutoField(primary_key=True)
    Product_id= models.ForeignKey(Product,on_delete=CASCADE)
    product_attribute_value_id= models.ForeignKey(Product_Attribute_values,on_delete=CASCADE)
    Product_Attribute_id= models.ForeignKey(Product_Attribute,on_delete=CASCADE)
   
    
class Coupons(CommonInfo):
    
    code = models.CharField(max_length=45,unique=True)
    # valid_from = models.DateTimeField()
    # valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(100)])
    active = models.BooleanField()
    no_of_uses = models.IntegerField("No of Uses:")

    def __str__(self):
        return self.code    


    
	