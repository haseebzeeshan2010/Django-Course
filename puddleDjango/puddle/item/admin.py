from django.contrib import admin

# Register your models here.
from.models import Category, Item # make sure to import your models and classes

admin.site.register(Category)
admin.site.register(Item) # to add it to the django admin GUI interface
