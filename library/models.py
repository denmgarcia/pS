from django.db import models


class Books(models.Model):
    isbn_no = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=50, blank=False)
    date_added = models.DateTimeField('date published')

    class Meta:
        verbose_name = "Book"

    def __str__(self):
        return self. isbn_no
