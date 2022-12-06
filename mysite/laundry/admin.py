from django.contrib import admin

from .models import Challan, Customer, Iteam, Service

# Register your models here.
admin.site.register(Customer)
admin.site.register(Challan)
admin.site.register(Iteam)
admin.site.register(Service)