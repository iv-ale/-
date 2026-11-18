from django.contrib import admin
from .models import Author, Book

admin.site.site_header = "магазин книг"
admin.site.site_title = "вдмин панель для книг"
admin.site.index_title = "книжный мэнэджмент"

class AuthorInline(admin.TabularInline):
    model = Author
    extra = 1
    fields = ("name", "country")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    list_filter = ("name", "country")
    search_fields = ("name", "country")
    list_per_page = 50

class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    fields = ("title", "author", "pages", "published_date", "genre")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pages", "published_date", "genre")
    list_filter = ("author", "genre", "published_date")
    search_fields = ("title", "author", "pages", "published_date", "genre")
    list_per_page = 25
    readonly_fields = ("published_date", "author", "genre")
    actions = [make_unavailable, make_available]

