from django.contrib import admin

# Register your models here.
from futbokas.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)