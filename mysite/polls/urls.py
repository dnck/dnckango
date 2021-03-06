#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'polls'

# note: the func path takes (route, view, kwargs, name)
urlpatterns = [path('', views.IndexView.as_view(), name='index'),
                path('<int:pk>/', views.DetailView.as_view(), name='detail'),
                path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
                path('<int:question_id>/vote/', views.vote, name='vote'),
                path('holyshit/', views.holyshit, name='holyshit'),#just for fun
                path('zoofun/', views.zoofun, {'censor': True}, name='zoofun'),#just for fun
                ]
