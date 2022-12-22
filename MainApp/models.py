from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=200)


class Country(models.Model):
    name = models.CharField(max_length=200)
    language = models.ManyToManyField(Languages)
