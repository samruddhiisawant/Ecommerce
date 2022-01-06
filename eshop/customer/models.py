import re
from django.db import models
from django.contrib.auth.models import User

from store.models import CommonInfo
from ckeditor.fields import RichTextField
from django.utils.safestring import  mark_safe
from django.contrib.flatpages.models import FlatPage
# Create new user
# create superuser


    

# class User(models.Model):
#     username = models.CharField(max_length=100,unique=True)
#     phone_number = models.CharField(max_length=100,default='123')
#     birth_date = models.DateField(null=True,blank=True,default='2021-01-01')
#     # status = models.CharField( max_length=15, choices=status.choices)
#     # fb_token = models.CharField(max_length=100,null=True,blank=True)
#     # # twitter_token = models.CharField(max_length=100,null=True,blank=True)
#     #google_token = models.CharField(max_length=100,null=True,blank=True)
#     #registration_method = models.CharField(max_length=20,choices=Social_Register.choices,null=True,blank=True)

    # @property   
    # def fullname(self):
    #     return self.first_name + ' ' + self.last_name 

    
class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
    email = models.EmailField(verbose_name="email", max_length=45, unique=True)
    first_name = models.CharField(max_length=45, unique=False)
    last_name = models.CharField(max_length=45, unique=False)
    date_joined = models.DateField(verbose_name='created at', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    password = models.CharField(verbose_name='password', max_length=45)
    phone = models.CharField(verbose_name='phone', max_length=10, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Profile(models.Model):
    NORMAL_REGISTRATION = 'N'
    GOOGLE_REGISTRATION = 'G'
    FACEBOOK_REGISTRATION = 'F'
    TWITTER_REGISTRATION = 'T'

    REGISTRATION_CHOICES = [
        (NORMAL_REGISTRATION, 'Normal'),
        (GOOGLE_REGISTRATION, 'Google'),
        (FACEBOOK_REGISTRATION, 'Facebook'),
        (TWITTER_REGISTRATION, 'Twitter'),
    ]

    fb_token = models.CharField(max_length=100, null=True, blank=True)
    twitter_token = models.CharField(max_length=100, null=True, blank=True)
    google_token = models.CharField(max_length=100, null=True, blank=True)
    registration_method = models.CharField(max_length=1, choices=REGISTRATION_CHOICES, default=NORMAL_REGISTRATION)
    user = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Customer.email


class Customer_Address(models.Model):
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Customer address"
        
        
        
class EmailTemplate(CommonInfo):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    subject =models.CharField(max_length=255)
    content=models.TextField(blank= True , null = True)
    class Meta:
        
        verbose_name = 'Email'
        
        
class Contact_us(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    contact_no=models.CharField(max_length=45,null=True,blank=True)
    message=models.TextField(blank= True , null = True)
    #note_admin=models.TextField(blank= True , null = True)
 
class status(models.TextChoices):
    Active ='Active',"Active"
    Deactive='Deactive',"Deactive"   
      
class Banner(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/")
    status=models.CharField(max_length=15,choices=status.choices)
    
    def __str__(self):
        return self.name
    
class Cms(FlatPage,CommonInfo):
    meta_title=models.TextField(null=True,blank=True)
    meta_description=models.TextField(null=True,blank=True)
    meta_keywords=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    
class  Config(CommonInfo):
    conf_key=models.CharField(max_length=45)
    conf_value=models.CharField(max_length=100)
    status=models.CharField(max_length=15,choices=status.choices)   
