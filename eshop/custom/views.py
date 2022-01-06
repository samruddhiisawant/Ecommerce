

from pdb import set_trace
from re import template
from typing import Counter
from django.forms import fields
from django.forms.forms import Form
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls.conf import path
from django.views.generic.edit import UpdateView
from customer.models import *
from store.models import *
from orders.models import *
from .forms import *
from django.views.generic import CreateView
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    order=UserOrder.objects.count()
    Cust=Customer.objects.count()
    prod=Product.objects.count()
    coup=Coupons.objects.count()
    
   
   
    context={'order':order,'Cust':Cust,'prod':prod,'coup':coup}
    return render(request,'custom/dashboard.html',context)
    
    
    

#register Page


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('custom/customer/')
    else:
        if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password') 
            
            user =authenticate(request,username=username , password=password) 
            
            if user is not None :
                login(request,user)
                return redirect('/custom/dashboard/')
            else:
                messages.info(request,'Username or Password is incorrect')
                
        context = {}
        return render(request,'custom/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('custom/dashboard/')
    else:
        form = CreateUserForm()
        print("method")
        if request.method == 'POST':
            
            form = CreateUserForm(request.POST)
            if form.is_valid():
            
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')
             
        context ={'form':form}
        return render(request,'custom/register.html',context)
    






#Customer views
# decorator required to access pages

@login_required(login_url='login')
def customer_view(request):
    form=Customer.objects.all()
    return render(request, 'custom/customer_table.html',{'form':form}) 

@login_required(login_url='login')
def customerAddress_view(request):
    res = Customer_Address.objects.all()
    print("haha,",res[0])
    return render(request, 'custom/customer_address.html',{'addr':res}) 
    


#Product
@login_required(login_url='login')
def product_view(request):
    res = Product.objects.all()
    return render(request,'custom/data.html',{'res':res})

def product_attr_view(request):
    res = Product_Attribute.objects.all()
    attr=Product_attribute_association.objects.all()
    return render(request,'custom/prod_attr.html',{'res':res,'attr':attr})

def create_attr(request):
    print("runnning")
    if request.method == "POST":
        form=Product_AttributeForm(request.POST)
        print("whatssupp")
        print(form.errors)
        
        if form.is_valid():
            print("hello world")
            form.save()
            print("save")
            return redirect('/custom/product')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
    else:
        form = Product_AttributeForm()
    context ={'form':form}
    return render(request,'custom/create_attribute.html',context)

def update_attr(request, id):
    
	res = Product_Attribute.objects.get(id=id)
	form = Product_AttributeForm(instance=res)

	if request.method == 'POST':
		form = Product_AttributeForm(request.POST, instance=res)
		if form.is_valid():
			form.save()
			return redirect('/custom/attributes/')

	context = {'form':form}
	return render(request, 'custom/create_attribute.html', context)

def delete_attr(request, id):
    res = Product_Attribute.objects.get(id=id)
    if request.method == "POST":
        res.delete()
        return redirect('/custom/attributes/')
    context = {'item':res}
    return render(request, 'custom/delete_attr.html', context)




def product_attr_assc_view(request):
    attr=Product_attribute_association.objects.all()
    return render(request,'custom/prod_attr_assc.html',{'attr':attr})



def product_attr_value_view(request):
    attr=Product_Attribute_values.objects.all()
    return render(request,'custom/attr_value.html',{'attr':attr})


def create_attr_value(request):
    print("runnning")
    if request.method == "POST":
        form=Product_Attribute_value_Form(request.POST)
        print("whatssupp")
        print(form.errors)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('/custom/attribut_value/')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
    else:
        form = Product_Attribute_value_Form()
    context ={'form':form}
    return render(request,'custom/create_attribute_value.html',context)

def update_attrvalue(request,id):
    res = Product_Attribute_values.objects.get(id=id)
    form = Product_Attribute_value_Form(instance=res)
    if request.method == 'POST':
        form = Product_Attribute_value_Form(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return redirect('/custom/attributes/')
    context = {'form':form}
    return render(request, 'custom/create_attribute_value.html', context)


def update_assoc(request,id):
    res = Product_attribute_association.objects.get(id=id)
    form = ProductAttributeAssocform(instance=res)
    if request.method == 'POST':
        form = ProductAttributeAssocform(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return redirect('/custom/assc/')
    context = {'form':form}
    return render(request, 'custom/create_assc.html', context)


def delete_assoc(request, id):
    res = Product_attribute_association.objects.get(id=id)
    if request.method == "POST":
        res.delete()
        return redirect('/custom/assc/')
    context = {'item':res}
    return render(request, 'custom/delete_assc.html', context)


def delete_attrvalue(request, id):
    res = Product_Attribute_values.objects.get(id=id)
    if request.method == "POST":
        res.delete()
        return redirect('/custom/attributes/')
    context = {'item':res}
    return render(request, 'custom/delete_attrvalue.html', context)

def create_attr_assoc(request):
    
    if request.method == "POST":
        form=ProductAttributeAssocform(request.POST)
        
        print(form.errors)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('/custom/assc/')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
    else:
        form = ProductAttributeAssocform()
    context ={'form':form}
    return render(request,'custom/create_assc.html',context)



def order_view(request):
    res = UserOrder.objects.all()
    return render(request,'custom/orders.html',{'res':res})

@login_required(login_url='login')
def create_Product(request):
    print("runnning")
    if request.method == "POST":
        
        form= ProductForm(request.POST)
        print("whatssupp")
        print(form.errors)
        
        if form.is_valid():
            print("hello world")
            form.save()
            print("save")
            return redirect('/custom/product')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
        
        
    else:
        form = ProductForm()
    context ={'form':form}
    return render(request,'custom/product_form.html',context)


'''class CreateProduct(CreateView):
    model = Product
    form_name= ProductForm
    template_name='custom/product_form.html'
    fields = '__all__'
'''
@login_required(login_url='login')
def update_product(request, id):
    
	res = Product.objects.get(id=id)
	form = ProductForm(instance=res)

	if request.method == 'POST':
		form = ProductForm(request.POST, instance=res)
		if form.is_valid():
			form.save()
			return redirect('/custom/product')

	context = {'form':form}
	return render(request, 'custom/product_form.html', context)


@login_required(login_url='login')
def delete_product(request, id):
    res = Product.objects.get(id=id)
    if request.method == "POST":
        res.delete()
        return redirect('/custom/product')
    context = {'item':res}
    return render(request, 'custom/delete_product.html', context)


@method_decorator(login_required, name='dispatch')   
class updateproduct(UpdateView):
    model=Product
    form_class = ProductForm
    template_name = 'custom/edit_product.html'
    
    def dispatch(self,request, *args, **kwargs):
        Category_formset = inlineformset_factory(Product,
                                                 SubCategories,
                                                 form=SubCategoryForm,
                                                 extra=1,can_delete=False)
        
        Attribute_Formset = inlineformset_factory(Product,Product_attribute_association,
                                                  form=ProductAttributeAssocform,extra=1,
                                                  can_delete=False)
        
        Image_formset = inlineformset_factory(Product,ProductImages,
                                              form=ProductImageForm,extra=1,
                                              can_delete=False)
        
        
        self.Product=self.get_object()
        self.Category_formset =Category_formset
        self.Attribute_Formset=Attribute_Formset
        self.Image_formset=Image_formset
        
        self.Category_formset=Category_formset(instance=self.Product)
        self.Attribute_Formset=Attribute_Formset(instance=self.Product)
        self.Image_formset=Image_formset(instance=self.Product)  
        
        return super(updateproduct,self).dispatch(request,*args,**kwargs)  
    
    def form_valid(self, form):
        Category_formset = self.Category_formset(self.request.POST,instance=self.Product)
        Attribute_formset = self.Attribute_Formset(self.request.POST,instance=self.Product) 
        Image_formset =self.Image_formset(self.request.POST,instance=self.Product) 
        if Category_formset.is_valid() and Attribute_formset.is_valid() and Image_formset.is_valid():
            Category_formset.save()
            Attribute_formset.save()
            Image_formset.save()
            
        return super(updateproduct,self).form_valid(form)
    
    def post(self,request,**kwargs):
    
        try:
            if request.POST.get('data') == 'Category':
                v = request.POST.get('value')
                Category.objects.filter(id=v).delete()
                return HttpResponseRedirect('/custom/editproduct/{}/'.format(self.kwargs['pk'])) 

            if request.POST.get('data') == 'Attribute':
                v = request.POST.get('value')
                Product_attribute_association.objects.filter(id=v).delete()
                return HttpResponseRedirect('/custom/editproduct/{}/'.format(self.kwargs['pk']))

            if request.POST.get('data') == 'Image':
                v = request.POST.get('value')
                ProductImages.objects.get(id=v).delete()
                return HttpResponseRedirect('/custom/editproduct/{}/'.format(self.kwargs['pk']))
            return super(updateproduct,self).post(request,**kwargs)
        except Exception as e:
            return HttpResponseRedirect('/custom/editproduct/{}/'.format(self.kwargs['pk']))
    
    def get_context_data(self, **kwargs):
        context = super(updateproduct,self).get_context_data(**kwargs)
        context['Category_formset']=self.Category_formset
        context['Attribute_Formset']=self.Attribute_Formset
        context['Image_formset']=self.Image_formset
        
        return context
    
    
             
  
        
        
        




#Category
@login_required(login_url='login')
def Category_view(request):
    cat = Category.objects.all()
    return render(request,'custom/category_table.html',{'cat':cat})


@login_required(login_url='login')
def create_category(request):
    if request.method == "POST":
        
        form= CategoryForm(request.POST)
        print("whatssupp")
        print(form.errors)
        
        if form.is_valid():
            print("hello world")
            form.save()
            print("save")
            return redirect('/custom/category')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
        
        
    else:
        form = CategoryForm()
    context ={'form':form}
    return render(request,'custom/categoryform.html',context)


@login_required(login_url='login')
def delete_category(request, id):
    cat = Category.objects.get(id=id)
    if request.method == "POST":
        cat.delete()
        return redirect('/custom/category')
    context = {'item':cat}
    return render(request, 'custom/deleteCatg.html', context)


@login_required(login_url='login')
def update_category(request, id):
    
	cat = Category.objects.get(id=id)
	form = CategoryForm(instance=cat)

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=cat)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'custom/categoryform.html', context)


#coupon 
@login_required(login_url='login')
def Coupon_view(request):
    coup= Coupons.objects.all()
    return render(request,'custom/coupon.html',{'coup':coup})

@login_required(login_url='login')
def Create_coupon(request):
    
    if request.method == "POST":
        
        form= Couponform(request.POST)
        print("whatssupp")
        print(form.errors)
        
        if form.is_valid():
            print("hello world")
            form.save()
            print("save")
            return redirect('/custom/coupons')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
        
        
    else:
        form = Couponform()
    context ={'form':form}
    return render(request,'custom/couponform.html',context)
    
       
@login_required(login_url='login')
def delete_coupon(request, id):
    cat = Coupons.objects.get(id=id)
    if request.method == "POST":
        cat.delete()
        return redirect('/custom/coupons')
    context = {'item':cat}
    return render(request, 'custom/deletecoup.html', context)

@login_required(login_url='login')
def update_coupon(request, id):
    
	cat = Coupons.objects.get(id=id)
	form = Couponform(instance=cat)

	if request.method == 'POST':
		form = Couponform(request.POST, instance=cat)
		if form.is_valid():
			form.save()
			return redirect('/custom/coupons')

	context = {'form':form}
	return render(request, 'custom/couponform.html', context)





#email
@login_required(login_url='login')
def Email(request):
    
    if request.method == "POST":
        
        form= Emailform(request.POST)
        print("whatssupp")
        print(form.errors)
        
        if form.is_valid():
            print("hello world")
            form.save()
            print("save")
            return redirect('/custom/email')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
            
            
    else:
        form = Emailform()
    context ={'form':form}
    return render(request,'custom/email.html',context)


def Contactus(request):
    cat = Contact_us.objects.all()
    return render(request,'custom/contactus.html',{'cat':cat})


def report(request):
   
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        print(fromdate)
        print(todate)
        # userdet=Customer.objects.raw('select id from customer_customer where date_joined between"'+fromdate+'" and "'+todate+'"')
        data=Customer.objects.filter(date_joined__gte=fromdate,date_joined__lte=todate)
        print(data)
        context={'userdet':data}
        return render(request,'custom/report.html',context)
    else:
        userdet=Customer.objects.all()
        context={'userdet':userdet}
        return render(request,'custom/report.html',context)
    
    
def salesreport(request):
       
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        print(fromdate)
        print(todate)
        # userdet=Customer.objects.raw('select id from customer_customer where date_joined between"'+fromdate+'" and "'+todate+'"')
        data=UserOrder.objects.filter(created_date__gte=fromdate,created_date__lte=todate)
        print(data)
        context={'userdet':data}
        return render(request,'custom/sales_report.html',context)
    else:
        userdet=UserOrder.objects.all()
        context={'userdet':userdet}
        return render(request,'custom/sales_report.html',context)


def orderinfo(request,id):
    order = UserOrder.objects.filter(id=id)
    items= OrderDetails.objects.filter(order=id)
    address=Customer_Address.objects.filter(cust_id=request.user)
    context={'address':address,'order':order,'items':items}
    return render(request,'custom/vieworder.html',context)



def Bannersview(request):
    ban=Banner.objects.all()
    context={'ban':ban}
    return render(request,'custom/banner.html',context)


def createbanner(request):
    
    if request.method == "POST":
        form=Bannerform(request.POST, request.FILES)
        
        print(form.errors)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('/custom/banner/')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
            
            messages.error(request, "Please fill in all the fields.")
    else:
        form = Bannerform()
    context ={'form':form}
    return render(request,'custom/createbanner.html',context)

def delete_banner(request, id):
    ban = Banner.objects.get(id=id)
    if request.method == "POST":
        ban.delete()
        return redirect('/custom/banner/')
    context = {'item':ban}
    return render(request, 'custom/deletebanner.html', context)

@login_required(login_url='login')
def update_banner(request, id):
    
	ban = Banner.objects.get(id=id)
	form = Bannerform(instance=ban)

	if request.method == 'POST':
		form = Bannerform(request.POST, instance=ban)
		if form.is_valid():
			form.save()
			return redirect('/custom/banner/')

	context = {'form':form}
	return render(request, 'custom/createbanner.html', context)



def ProductImageview(request):
    img=ProductImages.objects.all()
    context={'img':img}
    return render(request,'custom/productimge.html',context)

def CreateProductImage(request):
    if request.method == "POST":
        form=ProductImageForm(request.POST, request.FILES)
        
        print(form.errors)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('/custom/productimage/')
        else:
            import pdb;pdb.set_trace()
            print(form.errors)
            HttpResponseRedirect("ERROR")
            
            messages.error(request, "Please fill in all the fields.")
    else:
        form = ProductImageForm()
    context ={'form':form}
    return render(request,'custom/createproductimg.html',context)

@login_required(login_url='login')
def update_productimg(request, id):
    
	ban = ProductImages.objects.get(id=id)
	form = ProductImageForm(instance=ban)

	if request.method == 'POST':
		form = ProductImageForm(request.POST, instance=ban)
		if form.is_valid():
			form.save()
			return redirect('/custom/productimage/')

	context = {'form':form}
	return render(request, 'custom/createproductimg.html', context)

def delete_productimg(request, id):
    ban = ProductImages.objects.get(id=id)
    if request.method == "POST":
        ban.delete()
        return redirect('/custom/productimage/')
    context = {'item':ban}
    return render(request, 'custom/deleteproductimg.html', context)
    
    




    













