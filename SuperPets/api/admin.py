from django.contrib import admin
from .models import Producto, BrandModel

# Register your models here.
@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    readonly_fields = ('created', 'updated',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'amount', 'price')
    readonly_fields = ('created', 'updated',)

    class Media: #?Esta clase la utilizamos para volver responsivo el widget de ckeditor
        css = {
            'all':('products/css/custom_ckeditor.css',)
        }

admin.site.register(Producto, ProductoAdmin)
