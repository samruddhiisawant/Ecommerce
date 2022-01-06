from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Customer_Address)
admin.site.register(Contact_us)
admin.site.register(EmailTemplate)
admin.site.register(Banner)

