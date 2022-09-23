from django.contrib import admin
from .models import Account
from .models import GoodsInfo, favorite, Brand, Product, Cart

admin.site.register(Account)


admin.site.register(GoodsInfo)

admin.site.register(Brand)

admin.site.register(Product)

admin.site.register(Cart)