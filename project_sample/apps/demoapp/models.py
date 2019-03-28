# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
