from django.contrib import admin
from .models import Location, Product, Image
from django.utils.html import format_html

# Inline form for images
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Number of empty forms to show initially

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location')  # Display 'location' field
    search_fields = ('title',)
    inlines = [ImageInline]
    list_filter = ['location__location']

class ImageAdmin(admin.ModelAdmin):
    list_filter = ['product__title']


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'url', 'view_products')  # Add a column to show products
    search_fields = ('location',)

    # Custom method to create a link to view products for each location
    def view_products(self, obj):
        # Link to view all products for the selected location
        url = f"/admin/products/product/?location__id__exact={obj.id}"  # Adjust `app` to your app name
        return format_html('<a href="{}">View Products</a>', url)

    # Make the 'view_products' field clickable and usable in the list
    view_products.short_description = 'Products'

admin.site.register(Location, LocationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
