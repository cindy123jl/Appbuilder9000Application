from django.db import models


CODE_CHOICES = [
    ('C#', 'C#'),
    ('Python', 'Python'),
    ('SQL', 'SQL'),
    ('JavaScript', 'JavaScript'),
    ('HTML', 'HTML'),
]


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    code_language = models.CharField(verbose_name='Code Language', max_length=50, default="Python", choices=CODE_CHOICES)
    date_published = models.DateField(verbose_name='Date Published', blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
