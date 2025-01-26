from django.contrib import admin

from api.models import *

admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Product)