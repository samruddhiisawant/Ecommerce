"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import handler400, handler404
from django.conf.urls import url
from django.contrib import admin
from django.template.context_processors import static
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout

urlpatterns = [
    path('',include('frontend.urls')),
    #url('pages/', include('django.contrib.flatpages.urls')),
    path('custom/',include('custom.urls')),
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('customer/', include('customer.urls')),
    url('oauth/', include('social_django.urls', namespace='social')),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},
    name='logout'),
    path('', include('django.contrib.auth.urls')),
    
    
    

]

handler404='frontend.views.errorPage'


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
