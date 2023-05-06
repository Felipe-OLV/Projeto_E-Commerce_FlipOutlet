from django.contrib import admin

# Register your models here.

from .models import ClothingItem

admin.site.register(ClothingItem)