# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#发布会表
class Event(models.Model):
    name=models.CharField(max_length=100)
    limit=models.IntegerField()
    status=models.BooleanField()
    address=models.CharField(max_length=200)
    start_time=models.DateTimeField('events time')
    create_time=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event)
    realname=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    sign = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("event", "phone")

    def __unicode__(self):
        return self.realname