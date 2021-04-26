from django.contrib import admin

from .models import Category, Product, ProductParameters, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ProductParametersInline(admin.TabularInline):
    model = ProductParameters
    extra = 1


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("name", "description", "image", "category")
    list_editable = ("description", "image")
    list_filter = ("name", "category")
    list_per_page = 50
    list_display_links = ("name", "category")
    inlines = (CommentInline, ProductParametersInline)


@admin.register(ProductParameters)
class ProductParameters(admin.ModelAdmin):
    list_display = ("product_id", "price", "count")
    list_editable = ("price", "count")
    list_filter = ("product_id",)
    list_per_page = 50

