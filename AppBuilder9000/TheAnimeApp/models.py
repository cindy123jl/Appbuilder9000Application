from django.db import models


Rating_Choices = (
    ("1 Star", "1 Star"),
    ("2 Stars", "2 Stars"),
    ("3 Stars", "3 Stars"),
    ("4 Stars", "4 Stars"),
    ("5 Stars", "5 Stars"),
    ("6 Stars", "6 Stars"),
    ("7 Stars", "7 Stars"),
    ("8 Stars", "8 Stars"),
    ("9 Stars", "9 Stars"),
    ("10 Stars", "10 Stars"),
)


class Review(models.Model):
    AnimeName = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)
    Rating = models.CharField(max_length=20)
    Review = models.TextField(max_length=500)

    def __str__(self):
        return self.AnimeName + ': Rated ' + self.Rating

    objects = models.Manager()


class Person(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    passwd = models.CharField(max_length=20)
