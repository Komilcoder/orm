from django.contrib import admin
from .models import Client,Product,Post,Persons,Order

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','user','publish','status')
    # list_filter = ('title','author','publish','status')
    search_fields = ('title','status')
    prepopulated_fields = {'title':('status',)}
    ordering = ('status','publish')


@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = ('user','name','last_name','year','age')
    search_fields = ('name','age')
    ordering = ('name','age')


