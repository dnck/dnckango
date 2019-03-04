#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    # no  __init__ ??
    question_text = models.CharField(max_length=200) # the CharField needs the max_length argument, which is pretty useful for validation
    pub_date = models.DateTimeField('date published')  # you cna give the Field a new human readable name, if not supplied then the variable name will be used

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # this model has a relationship to the preceeding model iow the choice is related to the question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # default here is optional, but its useful

    def __str__(self):
        return self.choice_text
# There are all sorts of database relations one-to-one, many-to-many, many-to-one
