from django.contrib import admin
from .models import *
# Register your models here.
myModels = [Category,SubCategory,Product,Order,OrderItem]
admin.site.register(myModels)
