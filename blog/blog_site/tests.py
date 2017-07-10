# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from blog_site.models import Article, Category, Tag


# Create your tests here.
class ArticleTestClass(TestCase):

    #@mock.patch(blog_site.)
    def setUp(self):
        temp_article = Article.objects.create(title='temp_article', content='Ha Ha Ha!')
        new_article = temp_article.save()

        temp_tag = Tag.objects.create(name='temp_tag')
        temp_tag = temp_tag.save()
        
        temp_cat = Category.objects.create(name='temp_cat')
        temp_cat = temp_cat.save()

        temp_article.tags.add(temp_tag)
        temp_article.category.add(temp_cat)

    def test_article(self):
        temp_article = Article.objects.get(title='temp_article')
        self.assertEqual(temp_article.category, 'temp_cat')

        for tag in temp_article.tags.all:
            self.assertEqual(tag.name, 'temp_tag')
        
