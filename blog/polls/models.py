# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

#from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #@python_2_unicode_compatible
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'was post recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #@python_2_unicode_compatible
    def __str__(self):
        return self.choice_text

'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
'''

'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('Question',               {'fields': ['question_text']}),
        ('Date information', 
            {'fields': 
                ['pub_date'],
                'classes': ['collapse']
            }),
    ]
    inlines=[ChoiceInline]

'''