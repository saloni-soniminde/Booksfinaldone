from django.contrib import admin
from . models import Books, Author
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('title','price')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


admin.site.register(Books, BookAdmin)
admin.site.register(Author, AuthorAdmin)