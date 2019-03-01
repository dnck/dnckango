from django.urls import path
from . import views
urlpatterns = [path('', views.index, name='index'),
                path('zoofun/', views.zoofun, {'censor': True}, name='zoofun'),]
