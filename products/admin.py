from django.contrib import admin

# Register your models here.
from products.models import techProducts

admin.site.register(techProducts)