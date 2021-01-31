from django.contrib import admin

from .models import  userInfo,User,genre,book,cart

class userInfo_admin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email','age', 'contact','gender']
    list_filter = []

admin.site.register(userInfo,userInfo_admin)

class genre_admin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

admin.site.register(genre,genre_admin)

class book_admin(admin.ModelAdmin):
    list_display =[ 'name', 'price' ,'img','author','description']
    list_filter = ['name', 'price', 'author']

admin.site.register(book,book_admin)

