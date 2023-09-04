from django.contrib import admin
from.models import items

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','image')
# Register your models here.

admin.site.register(items,ItemsAdmin)