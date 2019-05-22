#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from .models import Question
# dnck fun stuff:
import time
from django.utils import timezone
from random import choice
from matplotlib.colors import cnames
hexcolors=list(cnames.values())


# # display a list of objects generic
"""
This needs to be changed. We need the front page to be a list of available surveys.
So, we will need a table in our tables for the survey-link relation
"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class SurveysView(generic.ListView):
    template_name = 'polls/surveys.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# display a detail page for a particular type of object
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        exclude any questions that are not yet published
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class AboutView(TemplateView):
    template_name = "polls/about.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # first get the choice
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You did not select a choice, mate.', })
    else:
        selected_choice.votes = F('votes') + 1 # eliminate race conditions!
        selected_choice.save() # save
        selected_choice.refresh_from_db()
        # Always return an HttpResponse Redirect after sccessfully dealing with POST data
        # this prevents data from being posted twice if a user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
