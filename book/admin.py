from django.contrib import admin
from book.models import Author, Book
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_date", "created_at")
    list_display_links = ("first_name", "last_name")
    search_fields = ("id", "first_name", "last_name")
    ordering = ("id", "first_name")


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "description", "author", "price", "count", "created_at")
    list_display_links = ("id", "title", "description", "author")

    # search_fields = ("id", "title", 'description', 'author')
