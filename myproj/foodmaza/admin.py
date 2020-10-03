from django.contrib import admin
from foodmaza.models import Admin, Customer, Category, sub_category, Item

admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(sub_category)
admin.site.register(Item)
