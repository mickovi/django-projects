from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username', 'categories__name', 'content')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    # Definimos un campo propio para mostrar las categorías
    def post_categories(self, obj):
        return ', '.join([category.name for category in obj.categories.all().order_by('name')])

    post_categories.short_description = 'Categorías'
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

