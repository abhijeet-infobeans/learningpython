from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('rating', 'author')
    list_display = ('id', 'title', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address_line1', 'address_line2', 'zip', 'phone')
    
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
