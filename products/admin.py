from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'get_categories',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

    def get_categories(self, obj):
        return ", ".join([c.friendly_name or c.name for c in obj.category.all()])
    get_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'comment')
    list_filter = ('rating', 'created_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)