from django.contrib import admin
from apps.core.models import Category, Tag, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'in_stock')
    list_display_links = ('title', 'price', 'category')
    list_editable = ('in_stock',)


# admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Product)
