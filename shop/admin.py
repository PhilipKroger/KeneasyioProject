from django.contrib import admin
from .models import Product, CategorySeason, CategorySize

admin.site.register(Product)
admin.site.register(CategorySeason)
admin.site.register(CategorySize)
