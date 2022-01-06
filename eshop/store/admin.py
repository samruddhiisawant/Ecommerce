from django.contrib import admin


from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Product_Attribute_values)
admin.site.register(Product_Attribute)
admin.site.register(Product_attribute_association)
admin.site.register(ProductImages)
admin.site.register(Coupons)
admin.site.register(SubCategories)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )


admin.site.register(Category, CategoryAdmin)