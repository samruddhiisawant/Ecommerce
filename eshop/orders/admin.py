from django.contrib import admin
from .models import*
# Register your models here.

class OrderItemAdmin(admin.TabularInline):
    model = OrderDetails
    fieldsets = [
        ('Product', {'fields': ['product'], }),
        ('Quantity', {'fields': ['quantity'], }),
        ('Size', {'fields': ['item_size'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ('product', 'quantity', 'price', 'item_size')
    can_delete = False
    max_num = 0


admin.site.register(UserOrder)
admin.site.register(OrderDetails)
admin.site.register(Wishlist)


