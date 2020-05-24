# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apiv1.models import Questions
from apiv1.models import ScheduledExam
from apiv1.models import SubmittedExam

admin.site.register(Questions)
admin.site.register(ScheduledExam)
admin.site.register(SubmittedExam)