from django.contrib import admin
from .models import Post, Contact, Comment, Product

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'created', 'updated']

admin.site.register(Post, PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sent']

admin.site.register(Contact, ContactAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'commented']

admin.site.register(Comment, CommentAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'created']

admin.site.register(Product, ProductAdmin)