from django.contrib import admin

from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'added_by')
    readonly_fields = ('created_date',)
    search_fields = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'added_by')
    readonly_fields = ('created_date',)
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)

admin.site.site_title = 'Админ-панель Test'
admin.site.site_header = 'Админ-панель Test'

# Register your models here.
