import admin_thumbnails
from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from product import models
from product.models import Categorie, Product, Image, Comment, Color, Size, Variant

# Register your models here.


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Categorie.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Categorie.objects.add_related_count(qs,
                                                 Product,
                                                 'category',
                                                 'products_count',
                                                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_count.short_description = 'Related products (for this specific category)'
    related_products_cumulative_count.short_description = 'Related products (in tree)'


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('id',)
    extra = 1


class ProductVariantsInline(admin.TabularInline):
    model = Variant
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'image_thumbnail']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline, ProductVariantsInline]
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('subject', 'comment', 'ip',
                       'user', 'product', 'rate', 'id')


class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'color_tag']


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'color',
                    'size', 'price', 'quantity', 'image_tag']


admin.site.register(Categorie, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Image, ImagesAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Variant, VariantsAdmin)
