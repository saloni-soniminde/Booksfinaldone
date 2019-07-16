from django.contrib import admin
from . models import Books
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','price')

admin.site.register(Books, BookAdmin)