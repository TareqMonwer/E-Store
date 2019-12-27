from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'author')


admin.site.register(Book, BookAdmin)
