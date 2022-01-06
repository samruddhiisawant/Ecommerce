from  django.urls import path
from . import views
from django.conf import settings
from .views import *
from frontend import views
from django.contrib.auth import views as auth_views

app_name ='frontend'

urlpatterns = [
    path('registerpage/',views.regisPage,name='registerpage'),
    path('loginpage/',views.loginacc,name='loginpage'),
    path('logoutpage/',views.logoutacc,name='logoutpage'),
    
    path('',views.home,name="home"),
    path('home/',views.home,name='home'),
    path('error/',views.errorPage,name='error'), # not working
    path('shop/',views.shopPage,name='shop'),
    
    path('blog/',views.blog,name='blog'),
    path('blog-single/',views.blogsingle,name='blog-single'),
    
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update/',views.updateItem,name='update'),
    path('contactus/',views.Contact,name='contactus'),
    
    path('productdetail/<int:id>/',views.ProductDetailView.as_view(),name='productdetail'),
    
    path('processorder/',views.processOrder,name='processorder'),
    path('account/',views.account,name='account'),
   
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="frontend/password_reset.html"),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="frontend/password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="frontend/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="frontend/password_reset_done.html"), name='password_reset_complete'),
    path('change_password/',auth_views.PasswordChangeDoneView.as_view(template_name="frontend/change_password.html"),name='change_password'),
    #path('pages/about/',views.about,name='about'),
    path('category/<int:id>/',views.CategoryDetailView.as_view(),name='category'),
    path('myorders/',views.MyOrdersView.as_view(),name='myorders'),
    path('addwishlist/',views.addwishlist,name='addwishlist'),
    path('wishlist/',views.WishlistView.as_view(),name='wishlist'),
    path('success/',views.success,name='success'),
    path('tracker/',views.tracker,name='tracker'),
    path('subscribe/',views.newsletter,name='subscribe'),
    path('sub/',views.subscribe,name='sub'),
    
    
   
    
    
    
    
]
