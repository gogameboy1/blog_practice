# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']