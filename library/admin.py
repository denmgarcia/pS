from django.contrib import admin
from library.models import Books


class BookAdmin(admin.ModelAdmin):
    class Meta:
        fields = Books
        
    list_display = [
            'isbn_no',
            'author',
            'subject',
            'date_added',
        ]


admin.site.register(Books, BookAdmin)