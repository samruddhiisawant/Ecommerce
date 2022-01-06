
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import DecimalValidator, MinValueValidator, MaxValueValidator

# Create your models here.

  
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.enums import Choices
from django.db.models.fields import DecimalField
from django.utils import translation, tree
from store.models import Product, CommonInfo
from customer.models import Customer
from store.models import Coupons



ORDER_STATUS = (
    ('Placed', 'Placed'),
    ('Paid', 'Paid'),
    ('Shipped', 'Shipped'),
    ('Out for Delivery','Out for Delivery'),
    ('Delivered', 'Delivered')
)

SHIPPING = (
    ('standard','standard'),
    ('fast','fast')

)

class UserOrder(models.Model):
    status = models.CharField(max_length=120,
                              choices=ORDER_STATUS,
                              default='created')
    date_ordered =models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
                              
    # cart = models.ForeignKey(Cart,
    #                          on_delete=models.PROTECT)
    
    customer= models.ForeignKey(User,blank=True,null=True,
                             on_delete=models.CASCADE)
    shipping_method =models.CharField(max_length=50,choices=SHIPPING,default='standard',null=True)
    AWB_NO = models.CharField(max_length=100,null=True)
    payment_gateway_id = models.IntegerField(null=True)
    transaction_id = models.CharField(max_length=100)
    
    created_date= models.DateField(auto_now=True,null=True)
    status=models.CharField(max_length=50,choices=ORDER_STATUS,default='placed',null=True)
    grand_total=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    shipping_charges=models.DecimalField(max_digits=12,decimal_places=2,null=True)
    coupon_id= models.ForeignKey(Coupons, blank=True, null=True, on_delete=models.CASCADE)
    billing_address_1 = models.CharField(max_length=100, blank=True,null=True)
    billing_address_2 = models.CharField(max_length=100, blank=True,null=True)
    billing_city = models.CharField(max_length=45, blank=True,null=True)
    billing_state = models.CharField(max_length=45, blank=True,null=True)
    billing_country = models.CharField(max_length=45, blank=True,null=True)
    billing_zipcode = models.CharField(max_length=45, blank=True,null=True)
    shipping_address_1 = models.CharField(max_length=100, blank=True,null=True)
    shipping_address_2 = models.CharField(max_length=100, blank=True,null=True)
    shipping_city = models.CharField(max_length=45, blank=True,null=True)
    shipping_state = models.CharField(max_length=45, blank=True,null=True)
    shipping_country = models.CharField(max_length=45, blank=True,null=True)
    shipping_zipcode = models.CharField(max_length=45, blank=True,null=True)


    class Meta:
        ordering = ['-created_date',]

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderdetails_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderdetails_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping=False
        orderitems= self.orderdetails_set.all()
        for i in orderitems:
            if i.product_id ==  False:
                shipping=False
        return shipping
    
   
        
    @property
    def subtotal(self):
        if self.coupon_id:
            value=self.get_cart_total-((self.get_cart_total*self.coupon_id.discount)/100)
            return value
    
    @property  
    def get_grand_total(self):
        #shipping_charges=self.id.shippingcharges
        if self.coupon_id:
            value=self.get_cart_total-((self.get_cart_total*self.coupon_id.discount)/100)
            return value
            
        else:
            value=self.get_cart_total
            return value
    
  
    
    

class OrderDetails(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Price',null=True)
    product_id= models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    price=models.CharField(max_length=10,blank=True,null=True)
    
    @property
    def get_total(self):
        total =self.product_id.price * self.quantity
        return total
    
   
    
    
    
    
        
    
class Wishlist(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    
    



    
