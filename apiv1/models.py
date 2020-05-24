# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStamp(models.Model):
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True

class Questions(TimeStamp):
	question = models.CharField(max_length = 200)
	description = models.TextField(null = True, blank = True)
	answer_a = models.TextField()
	answer_b = models.TextField()
	answer_c = models.TextField(null = True, blank = True)
	answer_d = models.TextField(null = True, blank = True)
	answer_e = models.TextField(null = True, blank = True)
	correct_answer = models.CharField(max_length = 1)

	def __str__(self):
		return self.question

class ScheduledExam(TimeStamp):
	user = models.ForeignKey(User)
	is_appeared = models.BooleanField(max_length = 1, default = False)

	def __str__(self):
		return self.user


class UserQueForeignKey(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Questions, related_name = 'submittedexam')

	class Meta:
		abstract = True

class SubmittedExam(UserQueForeignKey, TimeStamp):
	user_answer = models.CharField(max_length = 1)
	is_correct = models.BooleanField(max_length = 1)
	score = models.IntegerField()