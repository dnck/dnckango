from django.urls import path
from . import views
# path(route, view, kwargs, name)
urlpatterns = [path('', views.index, name='index'),
                path('zoofun/', views.zoofun, {'censor': True}, name='zoofun'),]
