from django.db import models
#add model word that takes in 4 different fields
class word(models.Model):
    word_name = models.CharField(max_length=75)
    word_definition = models.CharField(max_length=255)
    word_in_a_sentence = models.CharField(max_length=255)
    where_did_you_find_the_word = models.CharField(max_length=255, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.word_name
#add model etymology that takes in one drop down input, and another for the origin of the word (this field is related to word model by field word name)
class etymology(models.Model):
    word_name = models.ForeignKey(word, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.word_name





