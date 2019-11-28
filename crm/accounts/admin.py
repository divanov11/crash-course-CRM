from django.contrib import admin

#from .models import *
from . models import Customer, Order, Product

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)