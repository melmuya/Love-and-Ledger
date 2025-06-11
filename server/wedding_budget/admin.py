from django.contrib import admin
from .models import Budget, Category, Vendor, ExpenseItem

# Register your models here.
admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(ExpenseItem)
