from __future__ import unicode_literals

from django.db import models
from ..users.models import *
from models import *
# Create your models here.

class QuoteManager(models.Manager):
    def add(self, post):
        print post
#        single_user = User.objects.get(id = post['uid'])
        Quote.objects.create(quoted_by = post['quoted_by'],
                            message = post['message'],
                            posted_by = post['uid'])

class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
    posted_by =  models.IntegerField(blank=False, null=False)
#    posted_by = models.ForeignKey(User, related_name = "postedby")
