from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'url', 'views')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'views', 'likes')
    prepopulated_fields = {'slug': ('name',)}


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'website', 'picture')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
