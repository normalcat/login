from __future__ import unicode_literals

from django.db import models
from ..users.models import *
from models import *
# Create your models here.

class QuoteManager(models.Manager):
    def add_(self, post, uid):
        errors = []

        if len(post['quoted_by']) < 2:
            errors.append("Name should be longer than 2 characters\n")

        if len(post['message']) <2 :
            errors.append("Please type in the message\n")

        if not errors:
            single_user = User.objects.get(id = uid)
            Quote.objects.create(quoted_by = post['quoted_by'],
                                    message = post['message'],
                                    posted_by = single_user)
        return errors

    def favorite(self, post, uid):
        single_user = User.objects.get(id = uid)
        single_quote = Quote.objects.get(id = post['qid'])
        single_quote.liked_by.add(single_user)
        return single_quote


class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
    liked_by = models.ManyToManyField(User, related_name = "likes")
    posted_by = models.ForeignKey(User, related_name = "posts")
