from __future__ import unicode_literals

from django.db import models
from ..users.models import *
# Create your models here.

class FriendManager(models.Manager):
    def add_(self, post, uid):
        print uid
        print post['fid']
        single_user = User.objects.get(id = uid)
        x = Friend.objects.create(linked_by = single_user)
        print x
        friend = User.objects.get(id = post['fid'])
        x.friend_by.add(friend)
        print x.friend_by.objects

class Friend(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = FriendManager()
    friend_by = models.ManyToManyField(User, related_name = "friends")
    linked_by = models.ForeignKey(User, related_name = "links")
