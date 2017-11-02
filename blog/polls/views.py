# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect

#from django.core.urlresolvers import reverse

'''method 1'''
#from django.views import generic

#from django.template import loader

from .models import Question, Choice
from django.urls import reverse
# Create your views here.

def index(request):
    latest_question_list = Question.objects.all().order_by('question_text')
    context = { 'latest_question_list':latest_question_list }
    return render(request,'polls/index.html', context)
    #return HttpResponse('hello, you are at the polls index')
    '''
    latest_question_list = Question.objects.all().order_by('question_text')[:3]
    latest_question_list = Question.objects.filter(id='7')[:3]
    '''
#def index(request):
    
    #template = loader.get_template('polls/index.html')
    #pass data to view
    
    #return HttpResponse(template.render(context ,request))
'''
#Method 1
class index(generic.ListView):
    template_name="polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()'''
def pilihan(request):
    pilihan_jawapan = Choice.objects.all()
    context = { 'pj':pilihan_jawapan }
    return render(request, 'polls/index.html', context)

def question_details(request,question_id):
    '''context = { 'details': 'question details'}
    return render(request, 'polls/question_details.html', context)'''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/question_details.html', { 'question':question })

def detail(request, question_id):
    return HttpResponse('you are looking at the question %s'%question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    greeting ='hello jasvin'
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render (request, 'polls/question_details.html',{
            
            'question':question,
            'error_message':"you dont have selected any choice",
            'greets':greeting,   
        })
    else:
        selected_choice.votes +=1
        selected_choice.save() 
        return HttpResponseRedirect(reverse('polls:result', args=(question.id)))

def result(request, question_id):
    #return HttpResponse('you are viewing result at %s' %question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/vote.html', {'question':question})
    