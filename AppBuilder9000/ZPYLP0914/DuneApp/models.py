from django.db import models

class Book(models.Model):
    book_title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    published = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)
    followed_by = models.CharField(max_length=60)

    Books = models.Manager()

    def __str__(self):
        return self.book_title
