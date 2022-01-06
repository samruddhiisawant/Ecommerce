
from re import template
from django.db.models.fields.json import DataContains
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render,redirect
from django.views.generic.base import View
import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import*
from store.models import *
from orders.models import *
from customer.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import JsonResponse
import json 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators  import login_required
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags

def home(request):
    products=Product.objects.all()
    cat= Category.objects.all()
    context={'products':products,'cat':cat}
    return render(request,'frontend/index.html',context)


def loginacc(request):
    if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password') 
            
            user =authenticate(request,username=username , password=password) 
            
            if user is not None :
                login(request,user)
                return redirect('/shop')
            else:
                messages.info(request,'Username or Password is incorrect')
                
    context = {}
    return render(request,'frontend/loginpage.html',context)

def logoutacc(request):
    logout(request)
    return redirect('/loginpage/')

def regisPage(request):
    if request.user.is_authenticated:
        return redirect('/shop')
    else:
        form = CreateUserForm()
        print("method")
        if request.method == 'POST':
            print("post owrking")
            form = CreateUserForm(request.POST)
            if form.is_valid():
            
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                html_content = render_to_string('email/placed_order.html',{})
                text_content = strip_tags(html_content)
                send_mail(
                    'Here are your Order Details',
                    text_content,
                    settings.EMAIL_HOST_USER ,
                    [request.user.email],  #request.user.email
                    html_message=html_content,
                    fail_silently=False)
                
                send_mail(
                    'User Placed Order Details',
                    text_content,
                    settings.EMAIL_HOST_USER ,
                    ['harshsanjayagrawal89@gmail.com'],
                    html_message=html_content,
                    fail_silently=False)
        # return redirect('/success/')
    
       
                
                
                return redirect('loginpage')
            
             
        context ={'form':form}
        return render(request,'frontend/register.html',context)

def errorPage(request,exception):
    context={}
    return render(request,'frontend/404.html',context)

def shopPage(request):
    if request.user.is_authenticated:
        customer=request.user
        orders = UserOrder.objects.filter(customer=customer, complete=False)

        if not orders.exists():
            order = UserOrder.objects.create(customer=customer, complete=False)
        else:
            order = orders.last()

        #order,created = UserOrder.objects.get_or_create(customer=request.user,complete=False)
        items=order.orderdetails_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']
        
    cat=Category.objects.all()   
    products=Product.objects.all()
    context={'products':products,'cartItems':cartItems,'shippig':False,'cat':cat}
    
    return render(request,'frontend/shop.html',context)


def blog(request):
    context={}
    return render(request,'frontend/blog.html',context)


def blogsingle(request):
    context={}
    return render(request,'frontend/blog-single.html',context)


def cart(request):
    
    if request.user.is_authenticated:
               
        customer=request.user
        print(customer)
        #order,created = UserOrder.objects.get_or_create(customer=request.user, complete=False)
        # items=order.orderdetails_set.all()
        # queries the object if not found it creates the obj
        order = UserOrder.objects.filter(customer=customer, complete=False)

        if not order.exists():
            order = UserOrder.objects.create(customer=customer, complete=False)
        else:
            order = order.last()
        
        
        couponcode=request.GET.get('couponcode')
        coupon_code_msg=None
        coupon=None
        if couponcode:
            try:
                coupon=Coupons.objects.get(code=couponcode)
                order.coupon_id=coupon
                order.save()
                coupon_code_msg='Coupon code Applied'
                order.grand_total=order.get_grand_total
                print(order.get_grand_total)
                order.save()
            except:
                coupon_code_msg='Invalid Coupon code'
                order.coupon_id=coupon
                order.save()
                order.grand_total=order.get_grand_total
                order.save()
                
            
        # orders = UserOrder.objects.filter(customer=customer, complete=False)

        # if not orders.exists():
        #         order = UserOrder.objects.create(customer=customer, complete=False)
        # else:
        #         order = orders.last()
        items= order.orderdetails_set.all()# child object with parent obj 
        # print("items",items[0])
        cartItems=order.get_cart_items 
        # print("cart:",cartItems)
                 
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shippig':False}
        cartItems=order.get_cart_items
        return redirect('/error/')
    
      
    context={'items':items,'order':order,'cartItems':cartItems,'coupon_code_msg':coupon_code_msg,'coupon':coupon}
    return render(request,'frontend/cart.html',context)


def checkout(request):
    
 
    if request.user.is_authenticated:
               
        customer=request.user
        print(customer)
        #order,created = UserOrder.objects.get_or_create(customer=request.user, complete=False)# queries the object if not found it creates the obj
        orders = UserOrder.objects.filter(customer=customer, complete=False)
        if not orders.exists():
                order = UserOrder.objects.create(customer=customer, complete=False)
        else:
                order = orders.last()
        items= order.orderdetails_set.all()# child object with parent obj 
        cartItems=order.get_cart_items
        address=Customer_Address.objects.filter(cust_id=request.user)
        if request.method=="POST":
            x=request.GET.get('address1')
            print("a",x)
                  
    else:
        #empty cart for non logged in user
        items=[]
        order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=order.get_cart_items
   
    context={'items':items,'order':order,'cartItems':cartItems,'address':address}
    return render(request,'frontend/checkout.html',context)

def contactus(request):
    context={}
    return render(request,'frontend/contact-us.html',context)


    


class ProductDetailView(View):
    def get(self,request,id):
        products =Product.objects.filter(id=id)
        items=Product.objects.all()
        cat=Category.objects.all()
        context={'products':products,'items':items,'cat':cat}
        return render(request,'frontend/product-details.html',context)
    
def updateItem(request):
    #print(request.META)
        
    #print(request.body)
    data = json.loads(request.body)
    
    print("data:",data)
    productId = data['productId']
    action = data['action']
    
    print('Action:',action)
    print('productId:',productId)
    
    customer = request.user
    print("RUNNINFG")
    product = Product.objects.get(id=productId)
    print(product.id)
    
    
    #order, created = UserOrder.objects.get_or_create(customer=customer, complete=False)
    order = UserOrder.objects.filter(customer=customer, complete=False)
    if not order.exists():
            order = UserOrder.objects.create(customer=customer, complete=False)
    else:
            order = order.last()
                
    print(order)
    #import pdb; pdb.set_trace()
    orderItem, created = OrderDetails.objects.get_or_create(order=order,product_id_id=product.id)
    
    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
        
    elif action =='remove':
        orderItem.quantity =(orderItem.quantity - 1)
        
    elif action =='delete':
        orderItem.quantity=0
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    
    return JsonResponse('Item was added',safe=False)  #safe boolean parameter defaults to True. If it's set to False, any object can be passed for serialization (otherwise only dict instances are allowed




def processOrder(request):
    
    
    #print('Data:',request.body)
    transaction_id = datetime.datetime.now().timestamp()
    awb=datetime.datetime.now().timestamp()/5000000
    data=json.loads(request.body)
    
    
    if request.user.is_authenticated:
        customer=request.user
        order = UserOrder.objects.filter(customer=customer, complete=False)
        if not order.exists():
            order = UserOrder.objects.create(customer=customer, complete=False)
        else:
            order = order.last()
        
        total=float(data['form']['total'])
        transaction_id = datetime.datetime.now().timestamp()
       
        order.transaction_id=transaction_id
        order.AWB_NO=awb
        order.grand_total=order.get_grand_total
        order.shipping_charges=0   
            
        order.save()
        
        
        if total==order.get_cart_total:
            order.complete=True
        order.save()
        
        order = UserOrder.objects.get(id = order.id)
        item= order.orderdetails_set.all()
        address=Customer_Address.objects.filter(cust_id=request.user)
        html_content = render_to_string('email/placed_order.html',{'order':order,'total':total,'address':address,'item':item})
        text_content = strip_tags(html_content)
        send_mail(
            'Here are your Order Details',
            text_content,
            settings.EMAIL_HOST_USER ,
            [request.user.email],  #request.user.email
            html_message=html_content,
            fail_silently=False)
        
        send_mail(
            'User Placed Order Details',
            text_content,
            settings.EMAIL_HOST_USER ,
            ['harshsanjayagrawal89@gmail.com'],
            html_message=html_content,
            fail_silently=False)
        # return redirect('/success/')
    
        product=Product.objects.all()
        
        

   
    else:
        print('User is not logged in..')
    return JsonResponse('Payment submitted..', safe=False)




def success(request):
    
    return render(request,'frontend/success.html')
    


    
                
def account(request):
   
    try:
        customer = request.user
            
        Customer_Address.objects.get_or_create(cust_id = customer)

        order , created = UserOrder.objects.get_or_create(customer = customer, status = False)
        items = order.orderdetails_set.all()
        address_info = Customer_Address.objects.get(cust_id= customer)
        print(address_info)

        user_info = User.objects.get(username = customer)
        print('u',user_info)

        if request.method == 'POST':
            addressInf = UserOrder.objects.filter( customer= user_info) 
            print(addressInf)
            for x in addressInf:
                
                addressInfo = x
                
            print(addressInfo)
            fetch_address1 = request.POST.get('address1')
            print("f",fetch_address1)
            fetch_address2 = request.POST.get('address2')
            fetch_mobile_Number = request.POST.get('number')
            fetch_country = request.POST.get('country')
            fetch_state = request.POST.get('state')
            fetch_city = request.POST.get('city')
            fetch_zipcode = request.POST.get('postcode')
            fetch_email = request.POST.get('ship_email')
            print(fetch_email)
            

            addressInfo.shipping_address_1 = fetch_address1
            addressInfo.shipping_address_2 = fetch_address2
            addressInfo.shipping_country   = fetch_country
            addressInfo.shipping_state     = fetch_state
            addressInfo.shipping_city      = fetch_city
            addressInfo.shipping_zipcode   = fetch_zipcode
            user_info.phone_number         = fetch_mobile_Number
            user_info.email                = fetch_email
            addressInfo.save()
            user_info.save()

            messages.success(request,"INFORMATION ADDED SUCCESSFULLY")
        
        
            #addressInfo = user_order.objects.get(user_id = user_info)
            fetch_billing_address1 = request.POST.get('billing_address1')
            fetch_billing_address2 = request.POST.get('billing_address2')
            fetch_billing_country = request.POST.get('billing_country')
            fetch_billing_state = request.POST.get('billing_state')
            fetch_billing_city = request.POST.get('billing_city')
            fetch_billing_postcode = request.POST.get('billing_postcode')
            
            addressInfo.billing_address_1 = fetch_billing_address1
            addressInfo.billing_address_2 = fetch_billing_address2
            addressInfo.billing_country   = fetch_billing_country
            addressInfo.billing_state     = fetch_billing_state
            addressInfo.billing_city      = fetch_billing_city
            addressInfo.billing_zipcode  = fetch_billing_postcode
            addressInfo.save()


            #info user_addres
            
            address_info.address_1 = fetch_billing_address1
            print(address_info.address_1)
            address_info.address_2 = fetch_billing_address2
            address_info.country  =  fetch_billing_country
            address_info.state   =   fetch_billing_state
            address_info.city    =   fetch_billing_city
            address_info.zipcode  =  fetch_billing_postcode
            address_info.save()   
        

            return redirect('/checkout/')



        context = {
            'items':items,
            'order':order,
            'user_info':user_info,
            
        }
        return render(request,'frontend/account.html',context)
    except:
        return render(request,'frontend/account.html')

# def about(request):
#     context={}
#     return render(request,'flatpages/default.html',context)


class CategoryDetailView(View):
    def get(self,request,id):
        categ =Category.objects.filter(id=id)
        items=Product.objects.all()
        sub=SubCategories.objects.filter(category_id=id)
        
        context={'items':items,'categ':categ,'sub':sub}
        return render(request,'frontend/category.html',context)
    
class MyOrdersView(View):
    def get(self,request):
        customer=request.user
        order = UserOrder.objects.filter(customer=customer, complete=True)
        items=OrderDetails.objects.all
        context={'order':order,'items':items}
        return render(request,'frontend/myorders.html',context)
    
def addwishlist(request):
    data = json.loads(request.body)
    print("DAAAATAA",data)
    productId = data['productId']
    action = data['action']
    print(productId)
    customer= request.user
    product= Product.objects.get(id=productId)
    print(product)
    data={}
    checkwishlist=Wishlist.objects.create(product=product,customer=customer).count
    print(checkwishlist)
    if checkwishlist >= 0:
        data={
            'bool':False
            }
       
    

        
    
    
    return JsonResponse('Item was added to wishlist')


    
class WishlistView(View):
    def get(self,request):
        customer=request.user
        categ =Category.objects.all
        wishlist = Wishlist.objects.filter(customer=customer)

        if not wishlist.exists():
            order = Wishlist.objects.create(customer=customer)
        else:
            order = wishlist.last()
        items=Product.objects.all
        context={'wishlist':wishlist,'items':items}
                 
        return render(request,'frontend/wishlist.html',context)
    
def Contact(request):
    if request.method == "POST":
            
        form= ContactUsform(request.POST)
        print("whatssupp")
        print(form.errors)
        
        if form.is_valid():
            print("hello world")
            form.save()
            print("save")
            return redirect('/home/')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
            
            
    else:
        form = ContactUsform()
        context ={'form':form}
    return render(request,'frontend/contact-us.html',context)


def tracker(request):
    if request.method=="POST":
        
        orderId = request.POST.get('orderId')
        try:
            order = UserOrder.objects.filter(id=orderId,customer=request.user)
            
            list=UserOrder.objects.filter(customer=request.user)
            x=len(list)
            y=len(order)
            update = OrderDetails.objects.filter(order=orderId)
            context={'order':order,'list':list,'x':x,'update':update,'y':y}
            return render(request,'frontend/order_tracker.html',context)
        except:
            messages.error(request,"This Order Doesnot Exist.")
            return  render(request,'frontend/order_tracker.html')
        

    return render(request, 'frontend/order_tracker.html')


api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))

def newsletter(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Email received. thank You! ")

    return render(request, 'frontend/subscription.html')
    
    

    
    




    

