from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_year', 'quantity', 'available_quantity')
    list_filter = ('publication_year', 'created_at')
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('created_at', 'updated_at')
