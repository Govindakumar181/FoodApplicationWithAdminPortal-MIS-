  
from django.contrib import admin

from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','message','posting_date')

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id','profile','product','description','ratings')
