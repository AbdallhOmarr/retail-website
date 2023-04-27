from django.contrib import admin
from .models import *
# Register your models here.
myModels = [Category,SubCategory,Product,Order,OrderItem, Review]
admin.site.register(myModels)
