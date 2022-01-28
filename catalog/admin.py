from django.contrib import admin
from .models import *


@admin.register(Author)  # Декоратор @register
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)  # Декоратор @register
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)  # Декоратор @register
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        (
            'Экземпляры книг',
            {
                'fields': ('book', 'imprint', 'inv_nom')
            }
        ),
        (
            'Статус и окончание его действия',
            {
                'fields': ('status', 'due_back')
            }
        )
    )


# admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Status)
admin.site.register(Genre)
admin.site.register(Language)
