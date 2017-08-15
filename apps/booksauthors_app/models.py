# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'booksauthors_app'

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'booksauthors_app'

class BookAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(Book, null=False)
    author_id = models.ForeignKey(Author, null=False)
